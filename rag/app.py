import os
import json
import logging
import traceback
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
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
    raise HTTPException(status_code=500, detail="AI21 API key not found")

# Initialize AI21 client
client = AI21Client(api_key=ai21_api_key)

# Initialize FastAPI app
app = FastAPI()

class LogFileInput(BaseModel):
    file_path: str

def analyze_with_ai21(prompt, text):
    logger.debug(f"Sending request to AI21 for prompt: {prompt[:50]}...")
    try:
        full_prompt = f"{prompt}\n\nLog file:\n{text}"
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
        logger.debug("Received response from AI21")
        return response.completions[0].data.text.strip()
    except Exception as e:
        logger.error(f"Error in AI21 API call: {str(e)}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail="Error in AI21 API call")

def process_log_file(file_path, prompts):
    logger.info(f"Processing file: {file_path}")
    try:
        with open(file_path, 'r') as file:
            log_content = file.read()
        
        results = []
        for prompt_dict in prompts:
            prompt = prompt_dict['prompt']
            result = analyze_with_ai21(prompt, log_content)
            results.append({"prompt": prompt, "result": result})
        
        return results
    except Exception as e:
        logger.error(f"Error processing {file_path}: {str(e)}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")

# Load prompts from JSON file
try:
    with open('prompts_v2.json', 'r') as f:
        prompts = json.load(f)
    logger.debug("Prompts loaded successfully from prompts.json")
except Exception as e:
    logger.error(f"Error loading prompts.json: {str(e)}")
    logger.error(traceback.format_exc())
    raise HTTPException(status_code=500, detail="Error loading prompts file")

@app.post("/analyze_log")
async def analyze_log(log_input: LogFileInput):
    file_path = log_input.file_path
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Log file not found")
    
    results = process_log_file(file_path, prompts)
    
    return {"file": os.path.basename(file_path), "results": results}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)