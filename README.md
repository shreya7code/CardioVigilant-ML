# 🫀 CardioVigilant: Cardiovascular Decompensation Forecasting  

CardioVigilant is a machine learning–powered web application designed to **predict cardiovascular decompensation** and assist healthcare providers with early diagnosis and proactive intervention.  
Cardiovascular diseases remain the leading cause of death globally, and timely prediction can save lives while reducing the healthcare burden.  

Our system leverages advanced ML models to forecast the likelihood of heart disease based on patient health attributes (e.g., chest pain type, blood pressure, cholesterol, max heart rate). The application provides clinicians and patients with a **user-friendly interface** to input health data and receive instant predictions.  

---

## 🚀 Features
- Data preprocessing: cleaning, null handling, outlier detection, label encoding  
- Exploratory Data Analysis (EDA) to uncover key health patterns  
- Trained multiple models (Logistic Regression, Random Forest, ANN, SVM, KNN, XGBoost)  
- Final deployment with **Artificial Neural Network (ANN)** achieving ~90% training accuracy and ~85% validation accuracy  
- Flask-based web app with interactive form input & prediction results  
- Future extension: integration with wearables & real-time monitoring  

---

## 🛠️ Tech Stack
- **Languages & Libraries**: Python, NumPy, Pandas, Scikit-learn, TensorFlow/Keras, Matplotlib, Seaborn  
- **Web Framework**: Flask (with HTML/CSS templates)  
- **Deployment Artifacts**: Pickled model (`model.pkl`) from Phase 2 for inference  

---

## 📊 Dataset
- Source: Kaggle Heart Disease dataset  
- Attributes:  
  - Age, Sex  
  - Chest Pain Type  
  - Resting Blood Pressure  
  - Cholesterol  
  - Fasting Blood Sugar  
  - Resting ECG  
  - Maximum Heart Rate  
  - Exercise Angina  
  - ST Depression (Oldpeak)  
  - ST Slope  
  - Target: Heart Disease (1 = Yes, 0 = No)  

---

## ⚙️ Setup & Usage
Clone the repository and run locally:  

```bash
git clone https://github.com/<your-username>/CardioVigilant-ML.git
cd CardioVigilant-ML/src/phase_3
python app.py
```

## 📈 Results

**Best Model: Artificial Neural Network (ANN)**

- Training Accuracy: 90.6%

- Validation Accuracy: 85.3%

- Demonstrated strong generalization for unseen patient data


## 🔮 Future Work

- Real-time integration with wearable devices for continuous monitoring

- Personalized risk assessment using historical, genetic, and lifestyle d-ata

- Expansion to remote patient monitoring & alert systems



## 👩‍💻 Contributors

- Shreya Thakur

- Aishwarya Chand

- Prajakta Jhade


## 📚 References

Scikit-learn Documentation [https://scikit-learn.org/stable/]

TensorFlow Beginner Guide [https://www.tensorflow.org/tutorials/quickstart/beginner]

Academic research papers on ANN, decision forests, and cardiovascular prediction
Decision Tree – [https://developers.google.com/machine-learning/decision-forests/decision-trees]
Random Forest - [https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html]

✨ CardioVigilant: Bringing AI into healthcare for proactive heart disease management.