import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Heart Disease Dashboard",
    page_icon="❤️",
    layout="wide"
)

# Load CSV from GitHub repository
df = pd.read_csv("heart.csv")

st.title("❤️ Heart Disease Dashboard")

st.header("Dataset Preview")
st.dataframe(df.head())

# Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Records", len(df))

with col2:
    st.metric("Missing Values", int(df.isnull().sum().sum()))

with col3:
    st.metric("Duplicates", int(df.duplicated().sum()))

# Chart 1
st.header("Heart Disease Distribution")

fig, ax = plt.subplots()
sns.countplot(data=df, x="target", ax=ax)
st.pyplot(fig)

# Chart 2
st.header("Age Distribution")

fig, ax = plt.subplots()
sns.histplot(df["age"], bins=15, kde=True, ax=ax)
st.pyplot(fig)

# Chart 3
st.header("Cholesterol by Disease Status")

fig, ax = plt.subplots()
sns.boxplot(data=df, x="target", y="chol", ax=ax)
st.pyplot(fig)

# Chart 4
st.header("Age vs Maximum Heart Rate")

fig, ax = plt.subplots()
sns.scatterplot(
    data=df,
    x="age",
    y="thalach",
    hue="target",
    ax=ax
)
st.pyplot(fig)


age = st.sidebar.slider(
    "Age",
    20,
    80,
    50
)


sex = st.sidebar.selectbox(
    "Sex",
    ["Male", "Female"]
)

chol = st.sidebar.slider(
    "Cholesterol",
    100,
    600,
    250
)

cp = st.sidebar.selectbox(
    "Chest Pain Type",
    [0,1,2,3]
)

risk_patients = len(df[df["target"] == 1])

st.metric(
    "Patients with Heart Disease",
    risk_patients
)

st.metric(
    "Missing Values",
    int(df.isnull().sum().sum())
)


st.metric(
    "Duplicate Records",
    int(df.duplicated().sum())
)


training_mean = df["chol"].mean()

new_dataset_mean = 280

difference = abs(
    new_dataset_mean - training_mean
)

st.write(
    f"Training Mean: {training_mean:.2f}"
)

st.write(
    f"New Mean: {new_dataset_mean:.2f}"
)

st.write(
    f"Difference: {difference:.2f}"
)

if difference > 20:
    st.warning(
        "Potential Data Drift Detected"
    )
else:
    st.success(
        "No Significant Data Drift"
    )
