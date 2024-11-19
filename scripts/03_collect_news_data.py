import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Alpha Vantage API key
API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')

# Alpha Vantage API URL
BASE_URL = "https://www.alphavantage.co/query"

# Define the stock symbol you are interested in (for market sentiment, use a stock like "AAPL")
symbol = "AAPL"

# Function to fetch news data from Alpha Vantage
def fetch_news_alpha_vantage(symbol):
    params = {
        'function': 'NEWS_SENTIMENT',  # Endpoint to get news sentiment
        'symbol': symbol,
        'apikey': API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    
    # Log the response status and content for debugging
    print(f"Status Code: {response.status_code}")
    print(f"Response Content: {response.text[:500]}")  # Print first 500 characters of the response

    if response.status_code == 200:
        try:
            # Parse the JSON response
            data = response.json()
            print("Full API Response:", data)  # Log full API response for debugging

            # Check if 'feed' is in the response
            if "feed" in data:
                articles = data['feed']
                if articles:
                    # Filter articles with sufficient sentiment scores
                    filtered_articles = [
                        article for article in articles if float(article.get('overall_sentiment_score', 0)) >= 0.1
                    ]
                    if filtered_articles:
                        return filtered_articles
                    else:
                        print("No articles with sufficient sentiment score.")
                        return []
                else:
                    print("No articles found in the response.")
                    return []
            else:
                print("No 'feed' field in the response.")
                return []
        except Exception as e:
            print(f"Error parsing response: {e}")
            return []
    else:
        print(f"Error fetching news: {response.status_code}")
        return []

# Function to save articles to CSV
def save_articles_to_csv(articles):
    # Create a DataFrame from the list of articles
    if articles:
        df = pd.DataFrame(articles)
        # Save DataFrame to CSV in the 'data' folder
        file_path = 'data/market_sentiment_data.csv'
        df.to_csv(file_path, index=False)
        print(f"Articles saved to {file_path}")
    else:
        print("No articles to save.")

# Main function to execute the process
def main():
    # Fetch news articles related to the symbol
    articles = fetch_news_alpha_vantage(symbol)
    
    # Save articles to CSV if available
    save_articles_to_csv(articles)

# Run the script
if __name__ == "__main__":
    main()