import streamlit as st
import requests
import json
import os
import time
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re
from collections import Counter

# FastAPI endpoint URL
API_URL = "http://localhost:8000/analyze_log"

st.title("Log File Analyzer")

# File uploader
uploaded_file = st.file_uploader("Choose a log file", type="log")

def parse_log_file(file_content):
    # This is a basic parser and should be adapted to your log format
    log_entries = file_content.split('\n')
    parsed_logs = []
    for entry in log_entries:
        if entry:
            # Assuming format: [TIMESTAMP] [LOG_LEVEL] Message
            match = re.match(r'\[(.*?)\] \[(.*?)\] (.*)', entry)
            if match:
                parsed_logs.append({
                    'timestamp': match.group(1),
                    'log_level': match.group(2),
                    'message': match.group(3)
                })
    return parsed_logs

if uploaded_file is not None:
    # Get file details
    file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": f"{uploaded_file.size / 1024:.2f} KB"}
    
    # Display file details
    st.write("File Details:")
    st.json(file_details)
    
    # Save the uploaded file temporarily
    with open("temp_log_file.log", "wb") as f:
        f.write(uploaded_file.getvalue())
    
    # Read and parse log file
    with open("temp_log_file.log", "r") as f:
        file_content = f.read()
        char_count = len(file_content)
        parsed_logs = parse_log_file(file_content)
    
    st.success("File uploaded and parsed successfully!")
    st.write(f"Number of characters in the log file: {char_count}")
    st.write(f"Number of log entries: {len(parsed_logs)}")

    if st.button("Analyze Log"):
        # Prepare the request payload
        payload = {"file_path": "temp_log_file.log"}

        # Send POST request to FastAPI backend
        try:
            start_time = time.time()
            response = requests.post(API_URL, json=payload)
            end_time = time.time()
            processing_time = end_time - start_time
            
            response.raise_for_status()  # Raise an exception for bad status codes
            
            # Parse and display results
            results = response.json()
            st.subheader("AI21 Analysis Results")
            
            st.write(f"Processing Time: {processing_time:.2f} seconds")
            
            if isinstance(results, dict) and 'results' in results:
                for i, result in enumerate(results['results'], 1):
                    with st.expander(f"Result {i}"):
                        st.write(f"**Prompt:** {result['prompt']}")
                        st.write(f"**Result:** {result['result']}")
                
                # Display summary
                st.subheader("AI21 Analysis Summary")
                st.write(f"Total prompts processed: {len(results['results'])}")
                st.write(f"Average tokens per result: {sum(len(r['result'].split()) for r in results['results']) / len(results['results']):.2f}")
            else:
                st.warning("Unexpected result format. Here's the raw output:")
                st.json(results)

            # Additional Analyses
            st.subheader("Log Analysis")

            if parsed_logs:
                # Log Level Distribution
                log_levels = [log['log_level'] for log in parsed_logs]
                level_counts = Counter(log_levels)
                if level_counts:
                    fig, ax = plt.subplots()
                    ax.bar(level_counts.keys(), level_counts.values())
                    ax.set_title("Log Level Distribution")
                    ax.set_xlabel("Log Level")
                    ax.set_ylabel("Count")
                    st.pyplot(fig)
                else:
                    st.warning("No log levels found in the parsed logs.")

                # Word Cloud
                all_messages = ' '.join([log['message'] for log in parsed_logs if log['message']])
                if all_messages:
                    try:
                        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_messages)
                        fig, ax = plt.subplots()
                        ax.imshow(wordcloud, interpolation='bilinear')
                        ax.axis('off')
                        ax.set_title("Word Cloud of Log Messages")
                        st.pyplot(fig)
                    except ValueError as e:
                        st.warning(f"Could not generate word cloud: {str(e)}")
                else:
                    st.warning("No messages found to generate word cloud.")

                # Error Rate
                error_count = sum(1 for log in parsed_logs if log['log_level'] == 'ERROR')
                error_rate = error_count / len(parsed_logs) * 100
                st.write(f"Error Rate: {error_rate:.2f}%")

                # Time Series of Log Entries
                df = pd.DataFrame(parsed_logs)
                try:
                    df['timestamp'] = pd.to_datetime(df['timestamp'])
                    df.set_index('timestamp', inplace=True)
                    hourly_counts = df.resample('H').size()
                    if not hourly_counts.empty:
                        st.line_chart(hourly_counts)
                        st.write("Hourly Log Entry Count")
                    else:
                        st.warning("No data available for time series chart.")
                except (ValueError, KeyError) as e:
                    st.warning(f"Could not process timestamp data: {str(e)}")
            else:
                st.warning("No parsed logs available for analysis.")

        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred while communicating with the backend: {str(e)}")
        except json.JSONDecodeError:
            st.error("Failed to parse the response from the backend. The response might not be valid JSON.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")

        # Clean up the temporary file
        if os.path.exists("temp_log_file.log"):
            os.remove("temp_log_file.log")

st.write("Upload a log file and click 'Analyze Log' to get the analysis results.")