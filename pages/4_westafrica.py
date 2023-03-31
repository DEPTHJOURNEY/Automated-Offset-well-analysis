# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 12:30:04 2023

@author: Jayaraj
"""

import streamlit as st
import time
from PIL import Image
import base64
from streamlit_extras.switch_page_button import switch_page
st.set_page_config(layout='wide')

col1,col2 = st.columns([5,1])
shelf_logo = Image.open("F:/iadc-deep shah/shelf_icon.png")
with col1:
    st.header("RIGS JACKED UP IN WEST AFRICA REGION")
with col2:
    st.image(shelf_logo)
    
with st.container():
    #col1,col2,col3,col4,col5,col6,col7,col8,col9,col10 = st.columns(10)
    
    #with col1:
    col1,col2,col3,col4,col5 = st.columns(5)
    
    with col1:
        st.write("BALTIC")
        st.image(Image.open("F:/iadc-deep shah/rig icon/west africa/Baltic.jpg"))
        s1 = st.button("SUMMARY",key='1')
   
    
    with col2:
        st.write("MENTOR")
        st.image(Image.open("F:/iadc-deep shah/rig icon/west africa/SD-Mentor.jpg"))
        s2 = st.button("SUMMARY",key='2')
        
       
        
    with col3:
        st.write("AD")
        st.image(Image.open("F:/iadc-deep shah/rig icon/west africa/Shelf-Drilling-AD1.jpeg"))
        s3 = st.button("SUMMARY",key='3')
        
        
        
    with col4:
        st.write("TENACIOUS")
        st.image(Image.open("F:/iadc-deep shah/rig icon/west africa/Shelf-Drilling-Tenacious.jpg"))
        s4 = st.button("SUMMARY",key='4')
        #st.button("SUMMARY   ")
    with col5:
        st.write("TRIDENT-VIII")
        st.image(Image.open("F:/iadc-deep shah/rig icon/west africa/Trident-VIII.jpg"))
        s5 = st.button("SUMMARY",key='5')
        #st.button("SUMMARY    ")