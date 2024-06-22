import streamlit as st
import os
import sys

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

st.title("AI-Powered Log Analysis")

st.write("Welcome, This app is ready to process your log files.")

# File uploader
uploaded_file = st.file_uploader("Choose a log file", type="log")

# Prompt input
prompt = st.text_area("Enter your analysis prompt:", 
                      "Analyze this log file and provide a summary of key events, errors, and any unusual patterns.")

if uploaded_file is not None and prompt:
    st.write("File uploaded and prompt entered. Processing would start here.")
    st.write(f"File name: {uploaded_file.name}")
    st.write(f"Prompt: {prompt}")

st.write("App is ready for input.")