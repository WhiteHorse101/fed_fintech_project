import yfinance as yf
import pandas as pd
from datetime import datetime
import os

# Define fintech companies and date range
companies = {
    'PYPL': 'PayPal', 'SQ': 'Block', 'SOFI': 'SoFi',
    'ADYEN.AS': 'Adyen', 'WISE.L': 'Wise', 'NEXI.MI': 'Nexi',
    # 'APT.AX': 'Afterpay',  # Afterpay may be delisted
    'PAYTM.BO': 'Paytm', 'PDD': 'Pinduoduo'
}
start_date = "2018-01-01"
end_date = datetime.today().strftime('%Y-%m-%d')

# Initialize a list to collect data
all_data = []

# Loop through each company and fetch data
for ticker, company in companies.items():
    try:
        print(f"Fetching data for {company} ({ticker})")
        stock_df = yf.download(ticker, start=start_date, end=end_date)

        # Check if data was fetched successfully
        if not stock_df.empty:
            # Standardize columns to ensure consistency
            stock_df = stock_df[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]
            stock_df.columns = ['open', 'high', 'low', 'close', 'adj_close', 'volume']  # Set consistent column names
            stock_df['company'] = ticker  # Add ticker column for identification
            
            all_data.append(stock_df)  # Append only non-empty DataFrames
            print(f"Data collected for {company} ({ticker}): {stock_df.shape[0]} rows")

            # TEMPORARY: Save each ticker's data separately for verification
            os.makedirs('data/individual_stocks', exist_ok=True)
            stock_df.to_csv(f'data/individual_stocks/{ticker}_data.csv', index=False)
        else:
            print(f"Warning: No data found for {company} ({ticker}). It may be delisted or unavailable.")
    except Exception as e:
        print(f"Error fetching data for {company} ({ticker}): {e}")

# Combine all non-empty DataFrames into a single DataFrame
if all_data:
    # Concatenate all DataFrames in the list with consistent columns
    stock_price_df = pd.concat(all_data, ignore_index=True)
    
    # Save to CSV
    stock_price_df.to_csv('data/fintech_stock_prices.csv', index=False)
    print("Combined stock data saved to data/fintech_stock_prices.csv")
else:
    print("No stock data collected.")
