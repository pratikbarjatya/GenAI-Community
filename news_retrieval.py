import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def fetch_news(prompt):
    # Load the API key from the environment variables
    API_KEY = os.getenv("NEWS_API_KEY")
    if not API_KEY:
        raise ValueError("News API key is missing. Please check your .env file.")

    # Google News API Endpoint
    
    endpoint = f"https://newsapi.org/v2/everything"

    # Query the API with the user's prompt
    params = {
        "q": prompt,  # Search query based on user prompt
        "sortBy": "publishedAt",  # Sort by latest articles
        "pageSize": 5,  # Number of articles to retrieve
        "apiKey": API_KEY  # Your API key
    }

    response = requests.get(endpoint, params=params)

    # Parse the response
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        return [
            {
                "title": article["title"],
                "url": article["url"],
                "description": article.get("description", "No description available"),
                "source": article["source"]["name"],
            }
            for article in articles
        ]
    else:
        return [{"error": f"Failed to fetch news. Error: {response.json().get('message', 'Unknown error')}"}]
