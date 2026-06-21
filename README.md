# 🚗 Car Evaluation Predictor

Intern id : CITS1271

A Machine Learning web application built using Streamlit that predicts the acceptability of a car based on various vehicle attributes.

## 📌 Project Overview

This project uses Machine Learning algorithms to evaluate whether a car is:

* ❌ Unacceptable (unacc)
* ⚠️ Acceptable (acc)
* ✅ Good (good)
* 🚗 Very Good (vgood)

The application provides an interactive web interface where users can input car specifications and receive instant predictions.

---

## 🚀 Features

* Interactive Streamlit Web Application
* Real-Time Car Evaluation Prediction
* Prediction Probability Visualization
* Clean and User-Friendly Interface
* Machine Learning-Based Classification
* Download Prediction Report
* Feature Importance Analysis

---

## 📊 Dataset Information

**Dataset:** Car Evaluation Dataset

### Input Features

| Feature  | Description        |
| -------- | ------------------ |
| Buying   | Buying Price       |
| Maint    | Maintenance Cost   |
| Doors    | Number of Doors    |
| Persons  | Passenger Capacity |
| Lug Boot | Luggage Boot Size  |
| Safety   | Safety Rating      |

### Target Classes

* Unacceptable (unacc)
* Acceptable (acc)
* Good (good)
* Very Good (vgood)

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Joblib
* Matplotlib
* Seaborn

---

## 🤖 Machine Learning Models

The following models were trained and evaluated:

* Decision Tree Classifier
* Random Forest Classifier
* XGBoost Classifier
* CatBoost Classifier

### Best Performing Model

Random Forest Classifier

**Accuracy:** 99%+

---

## 📈 Exploratory Data Analysis

Performed:

* Data Cleaning
* Missing Value Analysis
* Duplicate Value Analysis
* Target Distribution Analysis
* Feature vs Target Analysis
* Correlation Analysis
* Feature Encoding



## 📂 Project Structure

```text
Car-Evaluation-Predictor/
│
├── app.py
├── car_model.pkl
├── car_evaluation.csv
├── requirements.txt
├── README.md
├── screenshots/
│   └── app.png
│
└── notebooks/
    └── car_model.ipynb
```

---

## 🎯 Future Improvements

* Model Hyperparameter Tuning
* Advanced Dashboard
* Cloud Deployment
* PDF Report Generation
* Model Explainability (SHAP)

---

## 👨‍💻 Author

**Himanshu Kumar**

B.Tech Computer Science Student
Android Developer | C++ Developer | Machine Learning Enthusiast

---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
