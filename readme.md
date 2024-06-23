# LogAgent

## Objective
LogAgent is a tool designed to help developers on production support by analyzing log files to debug issues that are difficult to reproduce, particularly logic or business flow issues that don't necessarily throw errors. It uses prompt engineering to guide an LLM in analyzing logs and identifying anomalies.

## Features
- **Log Analysis**: Reads and interprets log files to understand event flows and detect anomalies.
- **Prompt Engineering**: Utilizes complex prompts to guide the LLM in analyzing logs and outputting tokens for debugging.
- **Open Source**: Available for community use and contributions.

## Future Enhancements
- **RAG Pipeline**: Integrate a Retrieval-Augmented Generation pipeline for deeper codebase analysis and recommendations.
- **Large Log Support**: Expand capacity to handle logs larger than 256k tokens.
- **Reproduction and Fixes**: Provide steps to reproduce issues and suggest fixes using codebase references.

## Setup

### Local Setup
1. **Create Environment**:
    ```sh
    conda create -n log_analyzer python=3.10 -y
    conda activate log_analyzer
    ```

2. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the Server**:
    ```sh
    python app.py
    ```

4. **Run the Streamlit App**:
    ```sh
    streamlit run streamlit_app.py
    ```

## API Usage

### Example cURL Request
```sh
curl -X POST "http://localhost:8000/analyze_log" \
     -H "Content-Type: application/json" \
     -d '{"file_path": "/path/to/your/logfile.log"}' \
     > analysis_results.json
```

## Design Decisions
- **Backend**: FastAPI for robust API endpoints.
- **Frontend**: Streamlit for an intuitive user interface.
- **Log Analysis**: AI21's API to leverage advanced language models.
- **Asynchronous Processing**: Efficient handling of multiple requests in FastAPI.

## Assumptions
- Users have valid log files in a readable format.
- The AI21 API is accessible and functioning.
- Users have internet connectivity for app access and API communication.
- The system has sufficient resources to process logs and API requests.

## Limitations
- Only supports `.log` files.
- Analysis capabilities limited by the AI21 model.
- No persistent storage for analysis results.
- No user authentication or rate limiting.
- Memory constraints may limit log file size processing.

## Future Improvements
- User authentication and session management.
- Support for multiple file formats.
- Integration with additional AI models for comparative analysis.
- Caching and trend analysis over time.
- Graphical visualization of log analysis data.
- Batch processing for multiple log files.
- Customizable prompts for analysis.
- Improved error handling and user feedback.
- Export functionality for analysis results.

## Contribution
Contributions are welcome. Please fork the repository and submit pull requests.

---

By improving the README with clear sections on the objective, features, setup instructions, usage examples, design decisions, assumptions, limitations, and future improvements, users will have a comprehensive guide to understanding and using LogAgent.
