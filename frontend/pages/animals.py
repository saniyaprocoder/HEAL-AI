import streamlit as st

st.title("🐄 Animal Healthcare Module")

st.write("Enter animal symptoms and details.")

# Animal Details
animal_type = st.selectbox(
    "Select Animal Type",
    ["Cow", "Dog", "Goat", "Buffalo", "Other"]
)

animal_age = st.number_input(
    "Animal Age",
    min_value=0,
    max_value=50
)

symptoms = st.text_area(
    "Enter Symptoms"
)

# Image Upload
image = st.file_uploader(
    "Upload Wound/Image",
    type=["jpg", "png", "jpeg"]
)

# Submit Button
if st.button("Analyze Animal"):
    st.success("Animal data submitted successfully")