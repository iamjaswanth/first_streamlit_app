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
st.write(my_fruit_list) 




