AI-Powered Log Analysis System
This project implements an AI-powered log analysis system using AI21's language model API. The system is designed to analyze log files from various services and provide insights based on predefined prompts.
Getting Started
Prerequisites
Python 3.7+
AI21 API key
Installation
1. Clone the repository:
>
Install the required dependencies:
txt
Create a .env file in the project root and add your AI21 API key:
your_api_key_here
Usage
The main entry point for the application is exp.py. To run the log analysis:
py
This script will:
1. Load the AI21 API key from the environment variables
2. Process a single log file (currently set to "auth_service.log")
3. Analyze the log file using a predefined prompt
4. Output the analysis results
Project Structure
rag/: Main directory containing the core functionality
exp.py: Entry point for the experimental log analysis
rag.py: Contains the main log processing and AI21 API interaction logic
vector_db.py: Implements a vector database using ChromaDB for efficient log searching
prompts_v2.json: Contains predefined prompts for log analysis
sample_logs/: Directory containing sample log files for testing
requirements.txt: List of Python dependencies
Key Components
1. AI21 Integration: The system uses AI21's language model API for log analysis. The integration is handled in the analyze_with_ai21 function in rag.py.
Vector Database: ChromaDB is used as a vector database for efficient storage and retrieval of log entries. The implementation is in vector_db.py.
Log Processing: The process_log_file function in rag.py handles the reading and processing of log files.
Prompts: Analysis prompts are stored in prompts_v2.json and can be easily modified or extended.
Customization
To analyze different log files, modify the log_file variable in exp.py.
To add or modify analysis prompts, edit the prompts_v2.json file.
To adjust the AI21 model parameters, modify the analyze_with_ai21 function in rag.py.
Future Improvements
Implement multi-file analysis
Add a user interface for easier interaction
Integrate with real-time log streaming systems
Enhance error handling and logging
Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
License
This project is licensed under the MIT License - see the LICENSE file for details.