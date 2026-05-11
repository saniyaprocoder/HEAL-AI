import streamlit as st

st.title("🐄 Animal Healthcare Module")

st.write("Enter animal emergency details.")

st.markdown("---")

# Animal Details
animal_name = st.text_input("Animal Name")

animal_type = st.selectbox(
    "Animal Type",
    ["Cow", "Dog", "Goat", "Buffalo", "Other"]
)

animal_age = st.number_input(
    "Animal Age",
    min_value=0,
    max_value=50
)

# Animal Health Data
temperature = st.number_input(
    "Body Temperature",
    min_value=20.0,
    max_value=50.0
)

eating = st.selectbox(
    "Eating Properly?",
    ["Yes", "No"]
)

activity = st.selectbox(
    "Activity Level",
    ["Normal", "Low", "Very Low"]
)

# Symptoms
symptoms = st.text_area(
    "Enter Symptoms"
)

# Upload Image
image = st.file_uploader(
    "Upload Wound/Image",
    type=["jpg", "png", "jpeg"]
)

st.markdown("---")

if st.button("Analyze Animal Emergency"):

    if activity == "Very Low":
        st.error("🚨 HIGH EMERGENCY RISK")

    else:
        st.success("✅ Animal Stable")

    st.info("AI veterinary analysis feature coming soon")