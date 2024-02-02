import streamlit as st
from pandas_datareader import data as pdr
import yfinance as yf
import pandas as pd
import datetime
import time
import numpy as np

# Override yfinance with pandas_datareader's methods
yf.pdr_override()

# Function to get stock data and calculate metrics
def get_stock_metrics(stock):
    try:
        df = pdr.get_data_yahoo(stock + '.NS', start_date, end_date)
        returns = np.log(df['Close'] / df['Close'].shift(1))
        volatility = returns.std() * np.sqrt(252)
        df['SMA_50'] =  round(df['Adj Close'].rolling(window=50).mean(), 2)
        moving_average_50 = df["SMA_50"][-1]
        sharpe_ratio = ((returns.mean() * 252) - 0.06) / volatility
        median = df['Volume'].median()
        if median > 100:
            return {'Stock': stock, 'SHARPE': sharpe_ratio,'MA_50':moving_average_50}
    except Exception as e:
        st.error(f"Could not gather data on {stock}")
        st.error(str(e))
        return None

# Streamlit App
st.title("Momentum Investing")

# Set up dates
start_date = datetime.datetime.now() - datetime.timedelta(days=365)
end_date = datetime.date.today()

# Read tickers
tickers_micro = pd.read_csv("./ind_niftymicrocap250_list.csv") 
tickers = pd.concat([tickers_micro], ignore_index=True)

# Process tickers
my_list = []
for stock in tickers['Symbol']:
    result = get_stock_metrics(stock)
    if result:
        my_list.append(result)

# Create DataFrame
df = pd.DataFrame(my_list)
df['Ranked'] = df['SHARPE'].rank(ascending=False)
top_30_df = df.sort_values(by='SHARPE', ascending=False).iloc[:35]
# Display results in Streamlit
st.write("### Top 35 Momentum Stocks")
st.write(top_30_df)

# Optionally, you can save the results to a CSV file
# df.to_csv('top_stocks.csv', index=False)
