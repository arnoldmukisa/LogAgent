import streamlit as st
import requests
import json
import os

# FastAPI endpoint URL
API_URL = "http://localhost:8000/analyze_log"

st.title("Log File Analyzer")

# File uploader
uploaded_file = st.file_uploader("Choose a log file", type="log")

if uploaded_file is not None:
    # Save the uploaded file temporarily
    with open("temp_log_file.log", "wb") as f:
        f.write(uploaded_file.getvalue())
    
    st.success("File uploaded successfully!")

    if st.button("Analyze Log"):
        # Prepare the request payload
        payload = {"file_path": "temp_log_file.log"}

        # Send POST request to FastAPI backend
        try:
            response = requests.post(API_URL, json=payload)
            response.raise_for_status()  # Raise an exception for bad status codes
            
            # Parse and display results
            results = response.json()
            st.subheader("Analysis Results")
            
            for result in results['results']:
                st.write(f"**Prompt:** {result['prompt']}")
                st.write(f"**Result:** {result['result']}")
                st.write("---")

        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {str(e)}")

        # Clean up the temporary file
        os.remove("temp_log_file.log")

st.write("Upload a log file and click 'Analyze Log' to get the analysis results.")