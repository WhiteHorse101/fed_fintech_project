# Load necessary libraries
import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key from environment variable
FRED_API_KEY = os.getenv('FRED_API_KEY')

# Check if API key is loaded
if not FRED_API_KEY:
    raise ValueError("FRED_API_KEY not found. Please set it in the .env file.")

# Define parameters for the API request
series_id = 'FEDFUNDS'
start_date = '2018-01-01'
end_date = datetime.today().strftime('%Y-%m-%d')

# Build the FRED API request URL
url = 'https://api.stlouisfed.org/fred/series/observations'
params = {
    'series_id': series_id,
    'api_key': FRED_API_KEY,
    'file_type': 'json',
    'observation_start': start_date,
    'observation_end': end_date
}

# Send the API request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Convert the JSON response to a DataFrame
    data = response.json()['observations']
    fed_rate_df = pd.DataFrame(data)[['date', 'value']]
    fed_rate_df['date'] = pd.to_datetime(fed_rate_df['date'])
    fed_rate_df.rename(columns={'value': 'fed_funds_rate'}, inplace=True)
    print("Federal Reserve Data Collected Successfully!")
    print(fed_rate_df.head())
    
    # Save to CSV
    fed_rate_df.to_csv('data/fed_rate_decisions.csv', index=False)
    print("Data saved to data/fed_rate_decisions.csv")
else:
    # Print error message if request fails
    print("Error fetching data:", response.status_code)
    print("Response:", response.json())
