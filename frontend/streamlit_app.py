import streamlit as st
import requests

BACKEND_URL = "http://backend:8000"


st.set_page_config(page_title="Dataset Quality Checker", layout="wide")

st.title("Dataset Quality Checker")
st.write("Upload a CSV file to analyze its quality and download a cleaned version.")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    with st.spinner("Analyzing dataset..."):
        response = requests.post(
            f"{BACKEND_URL}/analyze/",
            files={"file": uploaded_file}
        )

    if response.status_code != 200:
        st.error("Failed to analyze dataset")
    else:
        data = response.json()

        # Quality Score
        st.subheader("Quality Score")
        st.metric(
            label="Overall Score",
            value=data["quality_score"]["score"],
            delta=data["quality_score"]["verdict"]
        )

        # Suggestions
        st.subheader("Recommendations")
        for rec in data["suggestions"]["recommendations"]:
            st.write("•", rec)

        # Dataset Profile
        st.subheader("Dataset Overview")
        st.json(data["profile"])

        # Download cleaned dataset
        dataset_id = data["dataset_id"]
        download_url = f"{BACKEND_URL}/download/{dataset_id}"

        st.subheader("Download Cleaned Dataset")
        st.markdown(
            f"[Click here to download cleaned CSV]({download_url})"
        )
