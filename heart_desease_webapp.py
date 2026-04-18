# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 20:35:05 2026

@author: moete
"""

import numpy as np 
import pickle
import streamlit as st

loaded_model=pickle.load(open('trained_model.sav','rb'))


def heart_desease_prediction(input_data):
    input_data_array = np.array(input_data)
    input_data_reshaped=input_data_array .reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)
    if prediction[0]==1:
      return "the person has heart desease"
    else :
      return "the person doesn't have heart desease"

def main():
    #giving a title
    st.title('Heart_desease Prediction Web App')
    
    age=st.text_input('Age in years')
    sex=st.text_input('1 = male; 0 = female')
    cp=st.text_input('Chest pain type')
    trestbps=st.text_input('Resting blood pressure (in mm Hg)')
    chol=st.text_input('Serum cholesterol in mg/dl')
    fbs=st.text_input('Fasting blood sugar > 120 mg/dl (1 = true; 0 = false)')
    restecg=st.text_input('Resting electrocardiographic results')
    thalachh=st.text_input('Maximum heart rate achieved')
    exang=st.text_input('Exercise induced angina (1 = yes; 0 = no)')
    oldpeak=st.text_input('ST depression (heart potentially not getting enough oxygen)')
    slope=st.text_input('The slope of the peak exercise ST segment')
    ca=st.text_input('Number of major vessels (0-3) colored by fluoroscopy')
    thal=st.text_input('Thalium stress result')
     
     
     #code for prediction
    diagnosis=''
     
     #creating a button for prediction
    if st.button('Heart-desease Test Result'):
         diagnosis=heart_desease_prediction([age,sex,cp,trestbps,chol,fbs,restecg,thalachh,exang,oldpeak,slope,ca,thal])
            
    st.success(diagnosis)    
     

if __name__=='__main__':
    main()

