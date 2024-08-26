# There are freeform text inputs with st.text_input(); 
# radio buttons, st.radio(); numeric inputs with st.number_input(); 
# and a dozen more that are extremely helpful for making Streamlit apps. 

import streamlit as st
import numpy as np

perc_heads = st.number_input(label = 'Enter your number', 
min_value = 0.0, max_value = 1.0, value = .5)  # 0.5 is the default value

st.write("Double of number is ", perc_heads*2)

user_text = st.text_input(label='Enter your name')
st.write("The entered number is ", user_text)