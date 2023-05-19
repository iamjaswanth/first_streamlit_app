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
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗Kale, Spinach & Rocket Smoothie')
st.text('🥑🍞Hard-Boiled Free-Range Egg')
my_fruit_list = pd.read_csv("./ind_niftymicrocap250_list.csv") 
st.write(my_fruit_list) 




