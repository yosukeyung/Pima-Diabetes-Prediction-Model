# 🩺 Diabetes Risk Predictor App

> An interactive Machine Learning web application built with Streamlit to predict the likelihood of diabetes based on medical diagnostic measurements.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine_Learning-F7931E.svg)

## 💡 About The Project

This project was developed as part of an **AI Bootcamp** portfolio. It utilizes a **Logistic Regression** model trained on the famous [Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database) from Kaggle. 

The application takes in 8 patient features (such as Glucose, BMI, Insulin, Age, etc.) and instantly predicts whether the patient is at risk of diabetes. It also includes comprehensive data preprocessing steps like handling missing values (using median/mode imputation) and capping extreme outliers for better model accuracy.

## ✨ Features

- **User-Friendly Interface:** Built with Streamlit for a seamless and responsive user experience.
- **Real-Time Prediction:** Enter patient diagnostic metrics and get instant prediction results.
- **Robust Preprocessing:** Handles missing data and removes outliers using the IQR method.
- **Data Visualization:** Exploratory data analysis and outlier distribution visualized with Matplotlib.

## 🛠️ Tech Stack

- **Language:** Python 🐍
- **Libraries:** Pandas, NumPy, Matplotlib, Joblib
- **Machine Learning:** Scikit-Learn (Logistic Regression)
- **Web Framework:** Streamlit 🌐

## 🚀 How to Run Locally

Follow these steps to run the application on your local machine:

### 1. Clone the repository
```bash
git clone [https://github.com/yosukeyung/Pima-Diabetes-Prediction-Model.git](https://github.com/yosukeyung/Pima-Diabetes-Prediction-Model.git)
cd diabetes-risk-predictor
```

### 2. Install Dependencies
Make sure you have Python installed. Then, install the required libraries by running:
```bash
pip install -r requirements.txt
```
### 3. Run the Streamlit App
Execute the following command in your terminal:
```bash
streamlit run app.py
```
The application will open automatically in your default web browser at http://localhost:8501.

## ☁️ Running on Google Colab (Optional)
If you prefer to run this project on Google Colab (as demonstrated in the Jupyter Notebook):
   1. Upload the main.ipynb and app.py files to Colab.
   2. Download the dataset using the Kaggle API.
   3. Run the notebook cells and use Cloudflare Tunnel (trycloudflare.com) to expose the Streamlit        local server to the public web.

## 👨‍💻 Author
Yosuke Yung
*CS Student @ BINUS UNIVERSITY*
