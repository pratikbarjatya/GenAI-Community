import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def log_error(message):
    """Logs error messages to a file."""
    with open("error_logs.txt", "a") as log_file:
        log_file.write(f"{message}\n")

def fetch_news(prompt):
    try:
        # Load the API key from the environment variables
        API_KEY = os.getenv("NEWS_API_KEY")
        if not API_KEY:
            raise ValueError("News API key is missing. Please check your .env file.")

        # Google News API Endpoint
        endpoint = f"https://newsapi.org/v2/everything"

        # Query the API with the user's prompt
        params = {
            "q": prompt,  # Search query based on user prompt
            "sortBy": "relevancy",  # Sort by latest articles
            
            "pageSize": 10,  # Number of articles to retrieve
            "apiKey": API_KEY  # Your API key
        }

        # Log the request details
        log_error(f"Fetching news with prompt: {prompt}, params: {params}")

        response = requests.get(endpoint, params=params)

        # Log the raw response
        log_error(f"API Response: {response.status_code}, {response.text}")

        # Parse the response
        if response.status_code == 200:
            articles = response.json().get("articles", [])
            log_error(f"Fetched {len(articles)} articles successfully.")
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
            error_message = response.json().get('message', 'Unknown error')
            log_error(f"Failed to fetch news. API Error: {error_message}")
            return [{"error": f"Failed to fetch news. Error: {error_message}"}]

    except Exception as e:
        error_message = f"Error in fetch_news: {e}"
        log_error(error_message)
        return [{"error": error_message}]
