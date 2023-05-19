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
st.write(my_fruit_list) 




