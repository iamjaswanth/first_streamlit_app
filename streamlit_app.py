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
my_fruit_list = pd.read_csv("./first_streamlit_app
                            /ind_niftymicrocap250_list.csv") 
#my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
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


def get_fruitLoadlist():
    with my_cnx.cursor() as my_cur:
      my_cur.execute("select * from fruit_load_list")
      return my_cur.fetchall()
   
if st.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  my_data_row = get_fruitLoadlist()
  st.dataframe(my_data_row)
      
def insert_row_snowfalke(newfruit):
   with my_cnx.cursor() as my_cur:
      my_cur.execute("insert into fruit_load_list values ('" + newfruit + "')")
      return "Thanks for adding" + newfruit
   
addMy_fruit = st.text_input('What fruit would you like to add?')  
if st.button('Add a fruit to the list'):
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  back_frm_function = insert_row_snowfalke(addMy_fruit)
  st.text(back_frm_function)




