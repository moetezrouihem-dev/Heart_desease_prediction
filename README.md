# ❤️ Heart Disease Prediction 

**[🌐 Live Demo](https://heart-disease-prediction-moetez.streamlit.app/)** | **[📊 Dataset on Kaggle](https://www.kaggle.com/datasets/mfarhaannazirkhan/heart-dataset)**
## 📌 Overview
This project is an end-to-end Machine Learning solution designed to predict whether a person has heart disease based on their medical attributes. It includes a complete pipeline (data exploration, preprocessing, and model training) and an interactive web application built with Streamlit that allows users to input medical data and get real-time predictions.

> **💡 Remark:** This application is designed for everyone. You don’t need any programming or technical knowledge — just enter the values and get instant predictions.

## ✨ Features
* **Interactive Web Interface:** A clean, user-friendly UI built with Streamlit.
* **Real-time Predictions:** Instantly predicts the presence of heart disease using a trained Machine Learning model (`RandomForestClassifier` as the best model).
* **Comprehensive Data Analysis:** Includes a detailed Jupyter Notebook outlining the exploratory data analysis (EDA), data visualization, and model selection process.

## 📊 Model Selection & Performance
During the development phase, multiple machine learning algorithms were trained and evaluated to find the most accurate predictive model.

The initial baseline accuracy scores for the evaluated models were:
* **Random Forest Classifier:** 95.50% 🏆
* **K-Nearest Neighbors (KNN):** 80.95%
* **Logistic Regression:** 72.48%

Given its superior baseline performance, the **Random Forest Classifier** was selected as the primary algorithm. To ensure the model was fully optimized, hyperparameter tuning was performed using both `RandomizedSearchCV` and `GridSearchCV`. The tuned Random Forest model maintained its robust accuracy and was serialized as the final production model for this web application.

## 🛠️ Technologies Used
* **Programming Language:** Python
* **Development Environment:** Anaconda Distribution, Spyder IDE, Jupyter Notebook
* **Web Framework:** Streamlit
* **Data Manipulation:** Pandas, NumPy
* **Data Visualization:** Matplotlib, Seaborn
* **Model Serialization:** Pickle

## 🩺 Medical Attributes Used for Prediction
The web app expects the following clinical inputs to generate a prediction:
* **Age:** Age in years
* **Sex:** `1` = Male; `0` = Female
* **Chest Pain Type** (`cp`): Ranging from 0 to 3
* **Resting Blood Pressure** (`trestbps`): In mm Hg
* **Serum Cholestoral** (`chol`): In mg/dl
* **Fasting Blood Sugar** (`fbs`): > 120 mg/dl (`1` = true; `0` = false)
* **Resting ECG** (`restecg`): Electrocardiographic results (0, 1, 2)
* **Maximum Heart Rate** (`thalachh`): Maximum heart rate achieved during exercise
* **Exercise Induced Angina** (`exang`): `1` = yes; `0` = no
* **ST Depression** (`oldpeak`): Induced by exercise relative to rest
* **Slope:** The slope of the peak exercise ST segment
* **Major Vessels** (`ca`): Number of major vessels (0-3) colored by fluoroscopy
* **Thalium Stress Result** (`thal`): `0` = normal; `1` = fixed defect; `2` = reversable defect

## 🚀 Installation and Setup

Follow these steps to run the project on your local machine.

**1. Clone the repository**
```bash
git clone [https://github.com/your-username/heart-disease-prediction.git](https://github.com/your-username/heart-disease-prediction.git)
cd heart-disease-prediction
```
**2. Create a virtual environment (Optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
**3. Install the dependencies**

```bash
pip install -r requiremenst.txt
```
**4. Update Model Path (If necessary)**
Make sure the path to `trained_model.sav` inside `heart_desease_webapp.py` points to the correct location in your local directory. It is currently set to an absolute path and should ideally be updated to a relative path:

```python
# Change from:
# loaded_model=pickle.load(open('C:/Users/moete/OneDrive/Tiedostot/deploying a model/trained_model.sav','rb'))
# To:
loaded_model=pickle.load(open('trained_model.sav','rb'))
````
**5. Run the Streamlit App**

```bash
streamlit run heart_desease_webapp.py
````
