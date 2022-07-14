import streamlit 
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('Resto Melle')
streamlit.header('Lunch Menu')
streamlit.text('🥑BLT/Avo Sandwhich')
streamlit.text('🧇Chicken & Waffles')
streamlit.text('🌪Twista Salad')
streamlit.text('🍕Spaghetti Pizza')
streamlit.header('🍍🍌Build your own fruit smoothie')
#import python pandas package 
#import pandas
#object my_fruit_list 
# CSV must be read by pandas from the S3 bucket, use read_csv to pull the data into dataframe 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#sets the index to Fruit column NOT NUMBERS
my_fruit_list = my_fruit_list.set_index('Fruit')
#pick select list here for smothie creation: (list from index index declared)
#manually adds avo and bana to list 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
#hides the giant table 
fruits_to_show = my_fruit_list.loc[fruits_selected]
#display table on page (was my fruit list) now just fruits to show 
streamlit.dataframe(fruits_to_show)
#create the repeatable code block (called a function) function starts with def: and returns:
def get_fruityvice_data(this_fruit_choice):
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      return fruityvice_normalized
    
#new section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("please select a fruit to get information.")
  else:
      back_from_function = get_fruityvice_data(fruit_choice)
      streamlit.dataframe(back_from_function)

except URLError as e:
    streamlit.error()

streamlit.header("The fruit load list contains:")
#Snowflake-related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("select * from fruit_load_list")
         return my_cur.fetchall()

# add a button to load fruit
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])      
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)
#connecting to snowflake
#allow the end user to add a fruit to the list 
def insert_row_snowflake(new_fruit):
     with my_cnx.cursor() as my_cur:
          my_cur.execute("insert into fruit_load_list values ('from streamlit')")
          return "Thanks for adding ", new_fruit

add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a Fruit to the list'):
      my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
      back_from_function = insert_row_snowflake(add_my_fruit)
      streamlit.text(back_from_function)
     
#dont run anything past while troubleshooting:
streamlit.stop()


#import snowflake.connector

add_my_fruit = _input('What fruit would you like to add?','jackfruit')
streamlit.write()

# this will not work but go wiith it for now

