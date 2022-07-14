import streamlit 

streamlit.title('Resto Melle')
streamlit.header('Lunch Menu')
streamlit.text('🥑BLT/Avo Sandwhich')
streamlit.text('🧇Chicken & Waffles')
streamlit.text('🌪Twista Salad')
streamlit.text('🍕Spaghetti Pizza')
streamlit.header('🍍🍌Build your own fruit smoothie')
#import python pandas package 
import pandas
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
#new section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)


#build new table for genus 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

streamlit.dataframe(fruityvice_normalized)
import snowflake.connector


