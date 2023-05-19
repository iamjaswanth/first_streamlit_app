from pandas_datareader import data as pdr
from pandas import ExcelWriter
import yfinance as yf
import pandas as pd
import datetime
import time
import numpy as np
yf.pdr_override()
import streamlit as st


st.title('Momentum Investing')
st.header('Know what you own, and know why you own it.')
my_fruit_list = pd.read_csv("./ind_niftymicrocap250_list.csv") 
index_name = '^NSEI' # NIFTY50
start_date = datetime.datetime.now()  - datetime.timedelta(days=365)
end_date = datetime.date.today()
exportList = pd.DataFrame(columns=['Stock', "RS_Rating", "50 Day MA", "150 Day Ma", "200 Day MA", "52 Week Low", "52 week High","CP"])
returns_multiples = []

# Index Returns
index_df = yf.download(index_name, start_date, end_date)
index_df['Percent Change'] = index_df['Adj Close'].pct_change()
index_return = (index_df['Percent Change'] + 1).cumprod()[-1]

# Find top 30% performing stocks (relative to the S&P 500)
for ticker in tickers['Symbol']:
    try:
        # Download historical data as CSV for each stock (makes the process faster)
        ticker = ticker + ".NS"
        df = pdr.get_data_yahoo(ticker, start_date, end_date)
    
        # Calculating returns relative to the market (returns multiple)
        df['Percent Change'] = df['Adj Close'].pct_change()
        stock_return = (df['Percent Change'] + 1).cumprod()[-1]
        
        returns_multiple = round((stock_return / index_return), 2)
        returns_multiples.extend([returns_multiple])
        
        print (f'Ticker: {ticker}; Returns Multiple against NIFTY50: {returns_multiple}\n')
    except:
         print(f"Could not gather data on {ticker}")
         
    
   

# Creating dataframe of only top 30%
rs_df = pd.DataFrame(list(zip(tickers['Symbol'], returns_multiples)), columns=['Ticker', 'Returns_multiple'])
rs_df['RS_Rating'] = rs_df.Returns_multiple.rank(pct=True) * 100
rs_df = rs_df[rs_df.RS_Rating >= rs_df.RS_Rating.quantile(.70)]
st.write(rs_df) 




