# 💓 Heart Disease Risk Predictor

An end-to-end machine learning web application that predicts heart disease risk using clinical data. Built with Scikit-learn and deployed via Streamlit, this system provides real-time cardiovascular risk assessment with probability scoring.

---

## 📌 Project Overview

Heart disease remains one of the leading causes of death globally. Early detection and risk assessment play a critical role in prevention and treatment.

This application:
- Accepts clinical and diagnostic inputs
- Uses a trained ML classification model
- Predicts heart disease risk (High / Low)
- Displays probability score
- Maintains session-based prediction history
- Provides a modern interactive UI

---

## 🧠 Machine Learning Details

- Problem Type: Binary Classification  
- Dataset: UCI Heart Disease Dataset  
- Model: (Update with your algorithm – Logistic Regression / Random Forest / etc.)
- Features Used:
  - Age
  - Sex
  - Chest Pain Type
  - Resting Blood Pressure
  - Serum Cholesterol
  - Fasting Blood Sugar
  - Resting ECG
  - Maximum Heart Rate Achieved
  - Exercise Induced Angina
  - ST Depression (Oldpeak)
  - ST Segment Slope
  - Number of Major Vessels
  - Thalassemia

Model file:
```
model.pkl
```

---

## 🖥️ Tech Stack

- Python
- NumPy
- Pandas
- Scikit-learn
- Streamlit
- Pickle

---

## 📂 Project Structure

```
heart-disease-risk-predictor/
│
├── app.py                        # Streamlit application
├── model.pkl                     # Trained ML model
├── heart.csv                     # Dataset
├── heart disease pred.ipynb      # Model training notebook
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/heart-disease-risk-predictor.git
cd heart-disease-risk-predictor
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

---

## 📊 Key Features

- Dark modern UI with gradient styling
- Real-time probability-based prediction
- High-risk / Low-risk classification
- Session-based prediction history tracking
- Cached model loading for performance
- Error handling for missing model file

---

## 📈 Suggested Improvements (If You Want This To Look Stronger)

- Add model evaluation metrics (Accuracy, Precision, Recall, ROC-AUC)
- Include confusion matrix visualization
- Add feature importance plot
- Deploy on Streamlit Cloud and attach live demo link
- Replace session storage with database logging

Without evaluation metrics, this looks like a demo project. With metrics + deployment, it becomes portfolio-grade.

---

## ⚠️ Disclaimer

This application is for educational and research purposes only.  
It is not a substitute for professional medical advice.

---

## 👨‍💻 Author

Satyam Kumar  
Machine Learning & AI Enthusiast
