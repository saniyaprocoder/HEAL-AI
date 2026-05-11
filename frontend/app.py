import streamlit as st

st.set_page_config(
    page_title="HEAL-AI",
    page_icon="🏥",
    layout="centered"
)

st.title("🏥 HEAL-AI")

st.subheader(
    "Rural Emergency Healthcare for Humans and Animals"
)

st.markdown("---")

st.write(
    "Use the sidebar to choose a healthcare module."
)

st.markdown("---")

st.info(
    "AI-powered emergency healthcare assistance system."
)
st.markdown("---")

st.subheader("📱 Scan QR for Emergency Access")

st.image(
    "assets/heal_ai_qr.png",
    width=250
)