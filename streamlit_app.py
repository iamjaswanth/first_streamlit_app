import streamlit as st
import pandas as pd
import snowflake.connector
import requests
from urllib.error import URLError


st.title('My Moms New healty Dinner')
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗Kale, Spinach & Rocket Smoothie')
st.text('🥑🍞Hard-Boiled Free-Range Egg')
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
st.dataframe(fruits_to_show)

def get_fruvityvise_data(thisfruitchoic):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
   fruityvise_normalised = pd.json_normalize(fruityvice_response.json())
   return fruityvise_normalised

st.header("Fruityvice Fruit Advice!")



try:
   fruit_choice = st.text_input('What fruit would you like information about?')
   if not  fruit_choice:
    st.error("Please select a fruit to get information")
   else :
     back_from_function = get_fruvityvise_data(fruit_choice)
     st.dataframe(back_from_function)
   
except URLError as e:
  st.error()
  
         
st.write('The user entered ', fruit_choice)

st.stop()


my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchall()
st.header("Hello from Snowflake:")
st.dataframe(my_data_row)
fruit_choice2 = st.text_input('What fruit would you like to add?','jackfruit')
st.write('Thanks for adding ', fruit_choice2)
my_cur.execute("insert into fruit_load_list values ('from streamlit')")



