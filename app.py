import streamlit as st
import joblib
import numpy as np

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("svm_model.pkl")

# If you used StandardScaler while training
# scaler = joblib.load("scaler.pkl")

st.set_page_config(
    page_title="Banknote Authentication",
    page_icon="💵"
)

st.title("💵 Banknote Authentication")
st.write("Predict whether a banknote is Genuine or Forged.")

st.divider()

# -----------------------------
# User Input
# -----------------------------

variance = st.number_input("Variance", value=0.0)
skewness = st.number_input("Skewness", value=0.0)
curtosis = st.number_input("Curtosis", value=0.0)
entropy = st.number_input("Entropy", value=0.0)

# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict"):

    features = np.array([[variance, skewness, curtosis, entropy]])

    # Uncomment if scaler was used
    # features = scaler.transform(features)

    prediction = model.predict(features)[0]

    if prediction == 0:
        st.success("✅ Genuine Banknote")
    else:
        st.error("❌ Forged Banknote")