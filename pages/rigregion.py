# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 19:30:30 2023

@author: Jayaraj
"""
import streamlit as st
import time
from PIL import Image
import base64
from streamlit_extras.switch_page_button import switch_page
st.set_page_config(layout='wide')
st.header("RIGS")
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.fineartamerica.com/images/artworkimages/mediumlarge/1/blurred-sunset-sky-and-ocean-irina-moskalev.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 


with st.container():
    #col1,col2,col3,col4,col5,col6,col7,col8,col9,col10 = st.columns(10)
    image = Image.open("F:/iadc-deep shah/rig icon/SDE3.jpg")
    #with col1:
    col1,col2,col3,col4,col5 = st.columns(5)
    
    with col1:
        st.image(image)
        s1 = st.button("SUMMARY",key='1')
        if s1:
            switch_page("test")
    with col2:
        st.image(image)
        st.button("SUMMARY",key='2')
    with col3:
        st.image(image)
        st.button("SUMMARY",key='3')
    with col4:
        st.image(image)
        st.button("SUMMARY",key='4')
        #st.button("SUMMARY   ")
    with col5:
        st.image(image)
        st.button("SUMMARY",key='5')
        #st.button("SUMMARY    ")
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.image(image)
        st.button("SUMMARY",key='6')
    with col2:
        st.image(image)
        st.button("SUMMARY",key='7')
    with col3:
        st.image(image)
        st.button("SUMMARY",key='8')
    with col4:
        st.image(image)
        st.button("SUMMARY",key='9')
    with col5:
        st.image(image)
        st.button("SUMMARY",key='10')
        
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.image(image)
        st.button("SUMMARY",key='11')
    with col2:
        st.image(image)
        st.button("SUMMARY",key='12')
    with col3:
        st.image(image)
        st.button("SUMMARY",key='13')
    with col4:
        st.image(image)
        st.button("SUMMARY",key='14')
    with col5:
        st.image(image)
        st.button("SUMMARY",key='15')
        