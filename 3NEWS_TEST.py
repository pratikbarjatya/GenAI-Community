import requests
from dotenv import load_dotenv
import os

load_dotenv()

def test_newsapi():
    API_KEY = os.getenv("NEWS_API_KEY")
    if not API_KEY:
        print("Error: News API key is missing.")
        return

    endpoint = "https://newsapi.org/v2/everything"
    params = {
        "q": "Technology",
        "sortBy": "publishedAt",
        "pageSize": 5,
        "apiKey": API_KEY
    }

    response = requests.get(endpoint, params=params)
    if response.status_code == 200:
        print("NewsAPI Response:", response.json())
    else:
        print(f"Error: {response.status_code} - {response.json()}")

test_newsapi()
