import json
import os

# this would take selected prompts from JSON file and load all the sample data from logs folder .log fortmat, generate a number of errors each of the prompt deetected in the log file.abs
# Load selected prompts from JSON file
with open('prompts.json') as json_file:
    prompts = json.load(json_file)

# Load sample data from logs folder
log_folder = '/path/to/logs/folder'
log_files = [file for file in os.listdir(log_folder) if file.endswith('.log')]

# Generate errors for each prompt detected in the log files
for prompt in prompts:
    for log_file in log_files:
        with open(os.path.join(log_folder, log_file)) as file:
            log_data = file.read()
            if prompt in log_data:
                # Generate errors for the prompt
                # Your code to generate errors goes here
                # For example, you can print the prompt and log file name
                print(f"Error generated for prompt '{prompt}' in log file '{log_file}'")
