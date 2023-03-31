# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 12:46:08 2023

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
    st.header("RIGS JACKED UP IN NORTH SEA REGION")
with col2:
    st.image(shelf_logo)

with st.container():
    #col1,col2,col3,col4,col5,col6,col7,col8,col9,col10 = st.columns(10)
    
    #with col1:
    col1,col2,col3,col4,col5 = st.columns(5)
    
    with col1:
        st.write("SOUTHWARK")
        st.image(Image.open("F:/iadc-deep shah/rig icon/north_sea/At-Southwark-from-GC3-3-200x140.jpg"))
        s1 = st.button("SUMMARY",key='1')
   
    
    with col2:
        st.write("LLOYD")
        st.image(Image.open("F:/iadc-deep shah/rig icon/north_sea/Noble-Lloyd-Noble-1-Copy-200x140.jpg"))
        s2 = st.button("SUMMARY",key='2')
        
       
        
    with col3:
        st.write("SAM HARTELY")
        st.image(Image.open("F:/iadc-deep shah/rig icon/north_sea/SamHartley-A-20x30-200x140.jpg"))
        s3 = st.button("SUMMARY",key='3')
        
        
        
    with col4:
        st.write("SAM TURNER")
        st.image(Image.open("F:/iadc-deep shah/rig icon/north_sea/SamTurner-Jul2019-3-200x140.jpg"))
        s4 = st.button("SUMMARY",key='4')
        #st.button("SUMMARY   ")
   