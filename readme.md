
# Log File Analyzer Project


## objective


The objective of this project is to create a log file analyzer that can process log files and provide insights into the data contained within them. The application will utilize AI21's API to analyze log files and extract relevant information such as log levels, timestamps, and log messages. The analysis results will be presented to the user in an easy-to-understand format, allowing them to quickly identify patterns, anomalies, and other useful information from the log data.

## Design Decisions

- Utilized FastAPI for the backend to create a robust and fast API endpoint
- Implemented Streamlit for the frontend to provide an intuitive user interface
- Used AI21's API for log analysis to leverage advanced language models
- Employed asynchronous processing in FastAPI to handle multiple requests efficiently
- Implemented file uploading in Streamlit for easy log file submission

## Assumptions

- Users have valid log files in a readable format

sample log file:

```log
[2024-06-22 23:50:01 UTC] [INFO] [SchedulerService] Starting nightly batch jobs
[2024-06-22 23:50:02 UTC] [DEBUG] [DatabaseService] Initiating connection pool
[2024-06-22 23:50:03 UTC] [INFO] [CacheService] Flushing expired cache entries
[2024-06-22 23:50:04 UTC] [DEBUG] [AuthService] Rotating API keys
[2024-06-22 23:50:05 UTC] [INFO] [MonitoringService] System health check started
```

- The AI21 API is accessible and functioning
- Users have internet connectivity to access the Streamlit app and for the app to communicate with the FastAPI backend
- The system running the application has sufficient computational resources to process log files and API requests

## Limitations

- Currently only supports .log file extensions
- Analysis is limited by the capabilities of the AI21 model
- The application doesn't persist analysis results; they are generated on-demand
- There's no user authentication or rate limiting implemented
- The size of log files that can be processed may be limited by memory constraints

## Future Improvements

- Implement user authentication and session management
- Add support for multiple file formats beyond .log files
- Integrate with other AI models or services for comparative analysis
- Implement caching to store and quickly retrieve previous analysis results
- Add visualization features to represent log analysis data graphically
- Implement batch processing for multiple log files
- Add customization options for prompts used in the analysis
- Improve error handling and provide more detailed feedback to users
- Implement a database to store analysis history and allow for trend analysis over time
- Add export functionality for analysis results in various formats (PDF, CSV, etc.)
----

## setup


### local setup

```bash

conda create -n log_analyzer python=3.10 -y

conda activate log_analyzer

pip install -r requirements.txt


```

- run the server

```bash
python app.py

```

- run the streamlit app

```bash
streamlit run streamlit_app.py
```



# api usage

### curl request

```bash
curl -X POST "http://localhost:8000/analyze_log" \
     -H "Content-Type: application/json" \
     -d '{"file_path": "/path/to/your/logfile.log"}'

```

save the output to a file:
```bash

curl -X POST "http://localhost:8000/analyze_log" \
     -H "Content-Type: application/json" \
     -d '{"file_path": "/path/to/your/logfile.log"}' \
     > analysis_results.json

```