import streamlit as st
import numpy as np
import pickle
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="💓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- UPDATED CSS FOR PRETTY DARK GRADIENT BACKGROUND ---
st.markdown("""
    <style>
    /* Full Page Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #312e81 100%);
        background-attachment: fixed;
    }

    /* Fix for sidebar background to match */
    [data-testid="stSidebar"] {
        background-color: rgba(15, 23, 42, 0.9);
    }

    /* Card Styling - Glassmorphism (Semi-transparent white) */
    .info-card, .metric-card, div[data-testid="stColumn"] > div {
        background-color: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 15px;
        color: white !important;
    }

    /* Text Color Adjustments for Dark Background */
    h1, h2, h3, h4, p, label, .stMarkdown {
        color: #f1f5f9 !important;
    }

    .section-header {
        color: #818cf8 !important;
        font-size: 22px;
        font-weight: 700;
        margin: 20px 0 10px 0;
        padding-bottom: 10px;
        border-bottom: 2px solid #6366f1;
    }

    /* Prediction Result Boxes */
    .prediction-box {
        padding: 25px;
        border-radius: 12px;
        margin: 20px 0;
        color: white !important;
    }
    .success-box {
        background-color: rgba(34, 197, 94, 0.2);
        border: 1px solid #22c55e;
    }
    .danger-box {
        background-color: rgba(239, 68, 68, 0.2);
        border: 1px solid #ef4444;
    }

    /* Button Styling */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white !important;
        font-weight: 600;
        padding: 15px;
        border-radius: 10px;
        border: none;
        transition: all 0.3s;
    }
    
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 10px 20px rgba(0,0,0,0.3);
    }
    </style>
""", unsafe_allow_html=True)

# Cache the model loading
@st.cache_resource
def load_model():
    try:
        with open("model.pkl", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        st.error("⚠️ Model file not found. Please ensure 'model.pkl' is in the same directory.")
        return None
    except Exception as e:
        st.error(f"⚠️ Error loading model: {str(e)}")
        return None

# Load model
model = load_model()

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/heart-with-pulse.png", width=100)
    st.title("ℹ️ About")
    st.info("AI-powered clinical screening tool.")
    st.markdown("---")
    if model:
        st.success("✅ Model Ready")
    else:
        st.error("❌ Model Offline")

# Main content
st.title("💓 Heart Disease Risk Assessment")
st.markdown("### Complete the form below for a clinical risk evaluation")

tab1, tab2, tab3 = st.tabs(["📋 Patient Information", "📊 Results History", "❓ Help"])

with tab1:
    if model is None:
        st.stop()
    
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        st.markdown('<p class="section-header">👤 Personal Information</p>', unsafe_allow_html=True)
        age = st.slider("**Age**", 1, 120, 50)
        sex = st.selectbox("**Sex**", ["Male", "Female"])
        
        st.markdown('<p class="section-header">🩺 Clinical Measurements</p>', unsafe_allow_html=True)
        trestbps = st.number_input("**Resting Blood Pressure** (mm Hg)", 80, 200, 120)
        chol = st.number_input("**Serum Cholesterol** (mg/dl)", 100, 600, 200)
        fbs = st.selectbox("**Fasting Blood Sugar** > 120 mg/dl", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
        thalach = st.slider("**Max Heart Rate Achieved**", 60, 220, 150)
        oldpeak = st.slider("**ST Depression**", 0.0, 6.0, 1.0, step=0.1)
    
    with col2:
        st.markdown('<p class="section-header">💉 Diagnostic Tests</p>', unsafe_allow_html=True)
        cp = st.selectbox("**Chest Pain Type**", [0, 1, 2, 3], format_func=lambda x: ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"][x])
        restecg = st.selectbox("**Resting ECG Results**", [0, 1, 2], format_func=lambda x: ["Normal", "ST-T Wave", "LV Hypertrophy"][x])
        exang = st.selectbox("**Exercise Induced Angina**", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
        slope = st.selectbox("**ST Segment Slope**", [0, 1, 2], format_func=lambda x: ["Upsloping", "Flat", "Downsloping"][x])
        ca = st.selectbox("**Major Vessels (0-3)**", [0, 1, 2, 3])
        thal = st.selectbox("**Thalassemia**", [0, 1, 2, 3], format_func=lambda x: ["Normal", "Fixed Defect", "Reversible Defect", "Unknown"][x])

    st.markdown("---")
    
    # Data Prep
    sex_bin = 1 if sex == "Male" else 0
    input_features = np.array([[age, sex_bin, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    
    if st.button("🔍 Analyze Risk"):
        with st.spinner("Processing..."):
            prediction = model.predict(input_features)[0]
            probability = model.predict_proba(input_features)[0][1]
            
            # History Session State
            if 'history' not in st.session_state: st.session_state.history = []
            st.session_state.history.append({'timestamp': datetime.now().strftime("%H:%M:%S"), 'age': age, 'sex': sex, 'prediction': prediction, 'probability': probability})
            
            if prediction == 1:
                st.markdown(f'<div class="prediction-box danger-box"><h2>⚠️ High Risk: {probability*100:.1f}%</h2>Consult a cardiologist immediately.</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="prediction-box success-box"><h2>✅ Low Risk: {probability*100:.1f}%</h2>Metrics are within healthy ranges.</div>', unsafe_allow_html=True)

# Footer logic remains the same...