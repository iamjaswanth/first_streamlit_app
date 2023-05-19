import streamlit as st
import pandas as pd
import snowflake.connector
import requests
from urllib.error import URLError


st.title('Momentum Investing')
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗Kale, Spinach & Rocket Smoothie')
st.text('🥑🍞Hard-Boiled Free-Range Egg')
my_fruit_list = pd.read_csv("./first_streamlit_app/ind_niftymicrocap250_list.csv") 
st.write(df) 




