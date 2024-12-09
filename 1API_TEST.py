import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def test_huggingface_api():
    # Hugging Face API endpoint for sentiment analysis
    api_url = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment"
    
    # Load API key from .env file
    api_key = os.getenv("HUGGING_FACE_API")
    if not api_key:
        print("Error: Hugging Face API key is missing. Please check your .env file.")
        return

    headers = {"Authorization": f"Bearer {api_key}"}

    # Define a sample input
    sample_prompt = "I am so happy and excited about this project!"

    # Send the request
    response = requests.post(api_url, headers=headers, json={"inputs": sample_prompt})

    # Output the response
    if response.status_code == 200:
        print("API Response:", response.json())
    else:
        print(f"Error: Status Code {response.status_code}")
        print("Error Details:", response.json())

# Run the test
test_huggingface_api()
