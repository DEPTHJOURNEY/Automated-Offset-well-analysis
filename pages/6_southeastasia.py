# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 13:01:42 2023

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
    st.header("RIGS JACKED UP IN SOUTH EAST ASIA REGION")
with col2:
    st.image(shelf_logo)

with st.container():
    #col1,col2,col3,col4,col5,col6,col7,col8,col9,col10 = st.columns(10)
    
    #with col1:
    col1,col2,col3,col4,col5 = st.columns(5)
    
    with col1:
        st.write("SDE3")
        st.image(Image.open("F:/iadc-deep shah/rig icon/south_east_asia/SDE3.jpg"))
        s1 = st.button("SUMMARY",key='1')
   
    
    with col2:
        st.write("SCEPTER")
        st.image(Image.open("F:/iadc-deep shah/rig icon/south_east_asia/SD-Scepter.jpg"))
        s2 = st.button("SUMMARY",key='2')
        
       
        
    with col3:
        st.write("CHAOPPHRAYA")
        st.image(Image.open("F:/iadc-deep shah/rig icon/south_east_asia/Shelf-Drilling-Chaophraya.jpg"))
        s3 = st.button("SUMMARY",key='3')
        
        
        
    with col4:
        st.write("KRATHONG")
        st.image(Image.open("F:/iadc-deep shah/rig icon/south_east_asia/Shelf-Drilling-Krathong.jpg"))
        s4 = st.button("SUMMARY",key='4')
        #st.button("SUMMARY   ")
