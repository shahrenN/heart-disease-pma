
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Heart Disease Prediction Dashboard")

st.success("Dashboard Running")

import streamlit as st



st.set_page_config(
    page_title="Heart Disease Dashboard",
    page_icon="❤️",
    layout="wide"
)



st.title("❤️ Heart Disease Prediction Dashboard")

st.markdown("""
This dashboard supports healthcare stakeholders in identifying
patients at risk of heart disease using Machine Learning.
""")



try:
    df = pd.read_csv("/heart.csv")
except FileNotFoundError:
    st.error("heart.csv not found.")
    st.stop()



try:
    model = joblib.load("model.pkl")
    model_loaded = True
except:
    model_loaded = False



st.sidebar.header("Patient Information")

age = st.sidebar.slider(
    "Age",
    min_value=20,
    max_value=80,
    value=50
)

sex = st.sidebar.selectbox(
    "Sex",
    [0, 1],
    format_func=lambda x: "Female" if x == 0 else "Male"
)

cp = st.sidebar.selectbox(
    "Chest Pain Type",
    [0, 1, 2, 3]
)

chol = st.sidebar.slider(
    "Cholesterol",
    min_value=100,
    max_value=600,
    value=250
)

predict_button = st.sidebar.button(
    "Predict Heart Disease Risk"
)



st.header("Prediction Result")

if predict_button:

    if model_loaded:

        sample = np.array([[
            age,      # age
            sex,      # sex
            cp,       # chest pain type
            120,      # trestbps
            chol,     # chol
            0,        # fbs
            1,        # restecg
            150,      # thalach
            0,        # exang
            1.0,      # oldpeak
            1,        # slope
            0,        # ca
            2         # thal
        ]])

        prediction = model.predict(sample)

        if prediction[0] == 1:
            st.error("⚠️ Heart Disease Risk Detected")
        else:
            st.success("✅ No Heart Disease Detected")

    else:
        st.warning("model.pkl not found")



st.header("Monitoring Metrics")


