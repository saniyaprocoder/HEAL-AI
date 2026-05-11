import streamlit as st
import numpy as np
import joblib
model = joblib.load("C:\\Users\\syeed\\OneDrive\\Desktop\\HEAL-AI\\models\\heart_model.pkl")

st.title("👨 Human Healthcare Module")
st.sidebar.header("Human Emergency Help")

st.sidebar.info(
    "Provide correct patient details for accurate emergency analysis."
)
st.write("Enter patient emergency details.")

st.markdown("---")

# Patient Details
patient_name = st.text_input("Patient Name")

age = st.number_input(
    "Age",
    min_value=0,
    max_value=120
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female", "Other"]
)
location = st.text_input(
    "Patient Location"
)
# Vital Signs
temperature = st.number_input(
    "Body Temperature (°C)",
    min_value=30.0,
    max_value=45.0
)

oxygen = st.number_input(
    "Oxygen Level (%)",
    min_value=50,
    max_value=100
)

pulse = st.number_input(
    "Pulse Rate",
    min_value=30,
    max_value=200
)

# Symptoms
symptoms = st.text_area(
    "Enter Symptoms"
)

# Upload Reports
report = st.file_uploader(
    "Upload Medical Report",
    type=["pdf", "png", "jpg"]
)

st.markdown("---")

if st.button("Analyze Human Emergency"):

    sample_data = np.array([
        [
            age,
            1,
            2,
            120,
            200,
            0,
            1,
            pulse,
            0,
            1.2,
            1,
            0,
            2
        ]
    ])

    prediction = model.predict(sample_data)

    if prediction[0] == 1:

        st.error("🚨 HIGH HEART DISEASE RISK")

        st.warning("📞 Connecting to nearby specialist doctor...")

        st.info("🚑 Ambulance request initiated")

        st.info("🏥 Nearest hospital notified")

    else:

        st.success("✅ LOW HEART DISEASE RISK")

        st.info("🩺 Continue regular monitoring")