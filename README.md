# Impact of U.S. Federal Reserve Announcements on Fintech Stock Volatility

## Project Overview
This project aims to analyze the impact of U.S. Federal Reserve interest rate announcements on the stock prices and volatility of fintech companies across America, Europe, and Asia-Pacific. By examining market sentiment, macroeconomic indicators, and stock price fluctuations, we seek to understand how these announcements influence fintech stocks in different regions.

## Project Objectives
- Analyze the impact of Federal Reserve interest rate announcements on fintech stock prices and volatility.
- Explore market sentiment surrounding announcements to see how public perception influences stock movements.
- Perform a regional comparison to observe how fintech stocks in the U.S., Europe, and Asia-Pacific react differently to these announcements.

## Scope
- **Time Period**: Data from the past 5 years, covering various economic cycles and interest rate changes.
- **Data Sources**:
  - **Federal Reserve Rate Decisions**: Collected from FRED and the Federal Reserve website.
  - **Stock Price Data**: Daily OHLC and volume data for selected fintech companies.
  - **Market Sentiment**: News and social media data, including sentiment analysis.
  - **Macro-Economic Indicators**: Contextual economic data like inflation and GDP growth from FRED and World Bank.

## Project Workflow

### Step 1: Define Project Scope and Objectives
- **Objective**: Study the relationship between Federal Reserve announcements and fintech stock volatility across major regions.
- **Scope**: Analyze data over the last 5 years for companies in the U.S., Europe, and Asia-Pacific.

### Step 2: Data Collection
#### 1. Federal Reserve Interest Rate Decision Data
   - **Source**: FRED API or Federal Reserve website.
   - **Data Fields**: Date of announcement, rate decision (e.g., rate hike, rate cut), and rate change.
   - **Storage**: Stored in PostgreSQL in a `fed_rate_decisions` table.

#### 2. Stock Price Data for Selected Fintech Companies
   - **Companies**:
      - **America**: PayPal, Block (Square), SoFi.
      - **Europe**: Adyen, Wise, Nexi.
      - **Asia-Pacific**: Afterpay, Paytm, Pinduoduo.
   - **Source**: Yahoo Finance API or Alpha Vantage.
   - **Data Fields**: Date, open, high, low, close, volume.
   - **Storage**: Stored in PostgreSQL in a `stock_prices` table.

#### 3. Market Sentiment Data from News and Social Media
   - **Sources**: NewsAPI and Twitter API.
   - **Data Fields**: Date, headline, content, sentiment score.
   - **Storage**: Stored in MongoDB for unstructured text data in `news_articles` and `social_media` collections.

#### 4. Macro-Economic Indicators for Contextual Analysis
   - **Source**: FRED or World Bank.
   - **Data Fields**: Date, indicator_type, and value.
   - **Storage**: Stored in PostgreSQL in an `economic_indicators` table.

### Step 3: Data Preprocessing and Transformation
   - **Sentiment Analysis**: Use NLP tools (VADER or TextBlob) to calculate sentiment scores for news articles and tweets.
   - **Data Cleaning**: Handle missing values, filter irrelevant data, and align dates.
   - **Data Aggregation**: Standardize data to ensure consistency across datasets, especially around Fed announcement dates.

### Step 4: Data Storage
   - **PostgreSQL**: Used for structured data storage:
      - `fed_rate_decisions`: Federal Reserve decision data.
      - `stock_prices`: Daily stock prices for fintech companies.
      - `economic_indicators`: Macro-economic indicator data.
   - **MongoDB**: Used for unstructured text data storage:
      - `news_articles`: Stores news headlines and articles with sentiment scores.
      - `social_media`: Stores tweets with sentiment scores.

### Step 5: Data Analysis
   - **Time-Series Analysis**: Analyze stock price changes and volatility around each Fed announcement.
   - **Sentiment Impact Analysis**: Evaluate how sentiment scores affect stock movements around announcement dates.
   - **Regional Comparison**: Compare reactions among fintech stocks in the U.S., Europe, and Asia-Pacific.

### Step 6: Visualization
   - **Time-Series Plots**: Visualize stock price changes around Fed announcements and overlay sentiment scores.
   - **Bar Charts and Heatmaps**: Show average sentiment and stock price changes.
   - **Interactive Dashboards**: Create interactive dashboards in Tableau or Power BI to visualize trends by region and company.
   