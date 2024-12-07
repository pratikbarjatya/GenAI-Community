import requests

def fetch_news(prompt):
    # Google News API Endpoint
    API_KEY = "9f87ec037ca344559626e8dd1126a5b2"
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
