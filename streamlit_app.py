import streamlit 

streamlit.title('Resto Melle')

streamlit.header('Lunch Menu')
streamlit.text('🥑BLT/Avo Sandwhich')
streamlit.text('🧇Chicken & Waffles')
streamlit.text('🌪Twista Salad')
streamlit.text('🍕Spaghetti Pizza')
streamlit.header('🍍🍌Build your own fruit smoothie')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#my_fruit_list = my_fruit_list.set_index('Fruit')

#pick select list here for smothie creation: 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#display table on page 
streamlit.dataframe(my_fruit_list)

