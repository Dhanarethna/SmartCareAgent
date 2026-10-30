import streamlit as st

st.set_page_config(
    page_title="SmartCare Agent",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 SmartCare Agent")
st.subheader("AI-Powered Healthcare Support")

st.info(
    "This prototype supports healthcare information review. "
    "It does not diagnose medical conditions or replace a doctor."
)

st.header("Patient Information")

symptoms = st.text_area(
    "Describe the symptoms",
    placeholder="Example: fever and headache"
)

medications = st.text_input(
    "Current medications",
    placeholder="Enter medication names"
)

duration = st.selectbox(
    "How long have the symptoms been present?",
    ["Select duration", "Less than 24 hours", "1–3 days", "More than 3 days"]
)

if st.button("Analyze Information"):
    if not symptoms.strip():
        st.warning("Please enter the symptoms.")
    else:
        st.write("### Patient information received")
        st.write("**Symptoms:**", symptoms)
        st.write("**Medications:**", medications or "Not provided")
        st.write("**Duration:**", duration)

        st.warning(
            "This is an initial prototype. No medical diagnosis "
            "or verified drug-interaction result has been generated."
        )