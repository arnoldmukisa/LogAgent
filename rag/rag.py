import os
import logging
from dotenv import load_dotenv
import ai21
import json

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()
logger.debug("Environment variables loaded from .env file")

# Get AI21 API key from environment variable
ai21.api_key = os.getenv("AI21_API_KEY")
if ai21.api_key:
    logger.debug("AI21 API key loaded successfully")
else:
    logger.error("Failed to load AI21 API key. Make sure it's set in the .env file.")

def get_complexity_score(text):
    logger.debug("Entering get_complexity_score function")
    prompt = f"""Analyze the following log file and rate its complexity on a scale of 1-10, where 1 is very simple and 10 is extremely complex. Provide a brief explanation for your rating.

Log file:
{text}

Complexity rating (1-10):"""

    logger.debug("Sending request to AI21 for complexity score")
    try:
        response = ai21.Completion.execute(
            model="j2-ultra",
            prompt=prompt,
            maxTokens=200,
            temperature=0.7,
        )
        logger.debug("Received response from AI21 for complexity score")
        return response.completions[0].data.text
    except Exception as e:
        logger.error(f"Error in get_complexity_score: {str(e)}")
        return None

def assess_log_quality(text):
    logger.debug("Entering assess_log_quality function")
    prompt = f"""Analyze the following log file and assess its quality based on the following criteria:
1. Clarity of information
2. Consistency in formatting
3. Useful details provided
4. Proper use of log levels
5. Timestamp accuracy

Provide a brief assessment for each criterion and an overall quality rating on a scale of 1-10, where 1 is poor quality and 10 is excellent quality.

Log file:
{text}

Quality assessment:"""

    logger.debug("Sending request to AI21 for quality assessment")
    try:
        response = ai21.Completion.execute(
            model="j2-ultra",
            prompt=prompt,
            maxTokens=300,
            temperature=0.7,
        )
        logger.debug("Received response from AI21 for quality assessment")
        return response.completions[0].data.text
    except Exception as e:
        logger.error(f"Error in assess_log_quality: {str(e)}")
        return None

# Read the log file
logger.debug("Attempting to read paste.txt")
try:
    with open('paste.txt', 'r') as file:
        log_content = file.read()
    logger.debug("Successfully read paste.txt")
except FileNotFoundError:
    logger.error("paste.txt not found in the current directory")
    exit(1)
except Exception as e:
    logger.error(f"Error reading paste.txt: {str(e)}")
    exit(1)

# Get complexity score
logger.info("Getting complexity score")
complexity_score = get_complexity_score(log_content)
if complexity_score:
    print("Complexity Assessment:")
    print(complexity_score)
else:
    logger.error("Failed to get complexity score")

print("\n" + "="*50 + "\n")

# Assess log quality
logger.info("Assessing log quality")
quality_assessment = assess_log_quality(log_content)
if quality_assessment:
    print("Quality Assessment:")
    print(quality_assessment)
else:
    logger.error("Failed to get quality assessment")

logger.debug("Script execution completed")