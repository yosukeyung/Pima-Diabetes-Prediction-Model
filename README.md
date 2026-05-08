# Diabetes Prediction Web App

## Description
This project is an end-to-end Machine Learning web application designed to predict the likelihood of diabetes in patients. The machine learning model was trained using the **Pima Indians Diabetes Database** sourced from Kaggle. The final model is deployed with a user-friendly interactive interface using Streamlit.

## Tech Stack
* **Language**: Python
* **Data Manipulation & Visualization**: Pandas, NumPy, Matplotlib
* **Machine Learning**: Scikit-Learn (Logistic Regression)
* **Web Framework**: Streamlit

## Dataset and Preprocessing
The model uses the `uciml/pima-indians-diabetes-database` from Kaggle. 
To ensure the model performs well, the following data preprocessing steps were implemented:
* **Missing Value Handling**: Replaced missing numerical values with their median.
* **Outlier Handling**: Detected and capped data outliers using the Interquartile Range (IQR) bounding method.

## Application Features
The web app allows users to input specific health metrics to get an instant prediction. The inputted features include:
* Pregnancies
* Glucose
* Blood Pressure
* Skin Thickness
* Insulin
* BMI
* Diabetes Pedigree Function
* Age

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
   cd your-repo-name
