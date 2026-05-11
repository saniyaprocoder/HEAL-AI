import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="HEAL-AI",
    page_icon="🏥",
    layout="centered"
)

# Main Title
st.title("🏥 HEAL-AI")

st.subheader("Rural Emergency Healthcare System")

st.write(
    "AI-powered healthcare assistance for both humans and animals."
)

st.markdown("---")

# Module Selection
st.header("Choose Healthcare Module")

col1, col2 = st.columns(2)

with col1:
    st.info("👨 Human Healthcare")
    
    if st.button("Open Human Module"):
        st.success("Human Healthcare Module Selected")

with col2:
    st.info("🐄 Animal Healthcare")
    
    if st.button("Open Animal Module"):
        st.success("Animal Healthcare Module Selected")

st.markdown("---")

st.caption("HEAL-AI © Hackathon Project")