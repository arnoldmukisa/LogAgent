import os
import json
import logging
import traceback
import time
from dotenv import load_dotenv
from ai21 import AI21Client
from ai21.models import Penalty

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()
logger.debug("Environment variables loaded from .env file")

# Get AI21 API key from environment variable
ai21_api_key = os.getenv("AI21_API_KEY")
if ai21_api_key:
    logger.debug("AI21 API key loaded successfully")
else:
    logger.error("Failed to load AI21 API key. Make sure it's set in the .env file.")
    exit(1)

# Initialize AI21 client
client = AI21Client(api_key=ai21_api_key)

def analyze_with_ai21(prompt, text):
    logger.debug(f"Preparing to send request to AI21 for prompt: {prompt[:50]}...")
    start_time = time.time()
    try:
        full_prompt = f"{prompt}\n\nLog file:\n{text}"
        logger.debug(f"Full prompt length: {len(full_prompt)} characters")
        
        logger.debug("Sending request to AI21 API...")
        response = client.completion.create(
            prompt=full_prompt,
            max_tokens=500,
            model="j2-ultra",
            temperature=0.7,
            top_p=1,
            top_k_return=0,
            stop_sequences=["##"],
            num_results=1,
            custom_model=None,
            count_penalty=Penalty(scale=0),
            frequency_penalty=Penalty(scale=0),
            presence_penalty=Penalty(scale=0),
        )
        end_time = time.time()
        duration = end_time - start_time
        logger.debug(f"Received response from AI21 in {duration:.2f} seconds")
        logger.debug(f"Response length: {len(response.completions[0].data.text)} characters")
        return response.completions[0].data.text.strip()
    except Exception as e:
        end_time = time.time()
        duration = end_time - start_time
        logger.error(f"Error in AI21 API call after {duration:.2f} seconds: {str(e)}")
        logger.error(traceback.format_exc())
        return None

def process_log_file(file_path, prompt):
    logger.info(f"Processing file: {file_path}")
    start_time = time.time()
    try:
        with open(file_path, 'r') as file:
            log_content = file.read()
        logger.debug(f"Log file size: {len(log_content)} characters")
        
        result = analyze_with_ai21(prompt, log_content)
        
        end_time = time.time()
        duration = end_time - start_time
        logger.info(f"Completed processing {file_path} in {duration:.2f} seconds")
        return result
    except Exception as e:
        end_time = time.time()
        duration = end_time - start_time
        logger.error(f"Error processing {file_path} after {duration:.2f} seconds: {str(e)}")
        logger.error(traceback.format_exc())
        return None

# Single prompt for experimentation
prompt = "Analyze this log file and provide a summary of key events, errors, and any unusual patterns."

# Single log file for experimentation
log_file = "auth_service.log"  # Replace with your log file name
logs_dir = 'sample_logs'
file_path = os.path.join(logs_dir, log_file)

if not os.path.exists(file_path):
    logger.error(f"Log file not found: {file_path}")
    exit(1)

total_start_time = time.time()

result = process_log_file(file_path, prompt)

total_end_time = time.time()
total_duration = total_end_time - total_start_time
logger.info(f"Total processing time: {total_duration:.2f} seconds")

# Output result
print("\n=== Analysis Result ===\n")
print(f"File: {log_file}")
if result:
    print(f"\nPrompt: {prompt}")
    print(f"Result:\n{result}")
else:
    print("  Failed to process this file")

logger.debug("Script execution completed")