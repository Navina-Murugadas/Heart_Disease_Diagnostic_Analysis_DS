import streamlit as st
import numpy as np
import pandas as pd
import pickle

model = pickle.load(open('model.pkl','rb'))

st.title('HEART DISEASE ANALYZER')

# Collect user input for prediction
age = st.slider("Age", 1, 100, 25)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"])
trestbps = st.slider("Resting Blood Pressure (mm Hg)", 94, 200, 120)
chol = st.slider("Cholesterol (mg/dl)", 126, 564, 200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["No", "Yes"])
restecg = st.selectbox("Resting ECG Result", ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"])
thalach = st.slider("Maximum Heart Rate", 71, 202, 150)
exang = st.selectbox("Exercise-Induced Angina", ["No", "Yes"])
oldpeak = st.slider("Old Peak value", 0.0, 10.0, 2.5)
slope = st.selectbox("ST Slope", ["Upsloping", "Flat", "Downsloping"])
ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia Type", ["Normal", "Fixed Defect", "Reversible Defect"])


if st.button('ANALYZE'):
    sex = 1 if sex == "Male" else 0
    cp = ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"].index(cp)
    fbs = 1 if fbs == "Yes" else 0
    restecg = ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"].index(restecg)
    exang = 1 if exang == "Yes" else 0
    slope = ["Upsloping", "Flat", "Downsloping"].index(slope)
    thal = ["Normal", "Fixed Defect", "Reversible Defect"].index(thal)
    
    input_data = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
    prediction = model.predict([input_data])[0]

    if prediction == 1:
        st.subheader("DEFECTIVE HEART - HAS HEART DISEASE")
    else:
        st.subheader("HEALTHY HEART - STAY HAPPY")
