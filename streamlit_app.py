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
#my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
import pandas as pd
import streamlit as st

df = pd.read_csv("./data/titanic.csv")  # read a CSV file inside the 'data" folder next to 'app.py'
# df = pd.read_excel(...)  # will work for Excel files

st.title("Hello world!")  # add a title
st.write(df) 




