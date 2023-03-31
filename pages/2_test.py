# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 20:31:22 2023

@author: Jayaraj
"""




import streamlit as st
import streamlit as st
import time
from streamlit_card import card
from PIL import Image
import base64
from streamlit_extras.switch_page_button import switch_page
import pandas as pd

path_1 = "F:/iadc-deep shah/IADC-LAST WELL/SHOWCASE/IADC_WELL_RPT_test.xlsx"
path_2 = "F:/iadc-deep shah/IADC-LAST WELL/SHOWCASE/IADC_WELL_RPT_rig_color.xlsx"
path_3 = "F:/iadc-deep shah/IADC-LAST WELL/SHOWCASE/IADC_WELL_RPT_reg_color.xlsx"
df_1 =  pd.read_excel(path_1)
df_2 =  pd.read_excel(path_2)
df_3 =  pd.read_excel(path_3)

df_3['date'] = pd.to_datetime(df_3['date']).dt.date
df_3  = df_3.sort_values(by='date',ascending=False)
last_date = df_3['date'].iloc[-1]
print(last_date)


date_select = df_3['date'].unique()
df_3['date'] = df_3['date'].astype(str)

north_image_img = Image.open("F:/iadc-deep shah/north_sea3.jpg")
south_east_asia = Image.open("F:/iadc-deep shah/south_east_asia3.jpg")
india = Image.open("F:/iadc-deep shah/india.jpg")
india2 = Image.open("F:/iadc-deep shah/india2.jpg")
india4 = Image.open("F:/iadc-deep shah/india4.jpg")
west_africa = Image.open("F:/iadc-deep shah/WESTAFRICA2.jpg")
menam = Image.open("F:/iadc-deep shah/MENAM2.jpg")
blank = Image.open("F:/iadc-deep shah/blank.jpg")
tile = Image.open("F:/iadc-deep shah/tile2.jpg")
tile2 = Image.open("F:/iadc-deep shah/tile3.jpg")
shelf_logo = Image.open("F:/iadc-deep shah/shelf_icon.png")

st.set_page_config(layout='wide')
#home = st.button("HOME")
#if home:
#    switch_page("rigregion")
#st.title("TEST")
#full_report = st.button('MASTER-REPORT')
with st.container():
    col1,col2,col3,col4,col5,col6 = st.columns([5.5,5,2.5,5,2.5,2.5])
    with col6:
        st.image(shelf_logo)
        date_selectbox = st.selectbox("DATE",df_3['date'].unique())
        

with st.container():
    col1,col2,col3,col4,col5,col6 = st.columns([2.5,5,2.5,5,2.5,5.5])
    #with col3:
        #st.image(north_image_img)
        #s1 = st.button("ENTER THE REGION",key='1')
    with col1:  
        st.image(tile2)
        st.image(tile)
        s1 = st.button("CLICK TO ENTER",key='1')
        if s1:
            switch_page("southeastasia")
        
        
        df_3_temp = df_3   
        df_3_temp = df_3_temp[df_3_temp['date']==date_selectbox]
        df_3_temp = df_3_temp[df_3_temp['region_name']=='SOUTH EAST ASIA']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        st.text(south_east_asia_write)
    with col2:
        st.image(south_east_asia)
    with col3:
        st.image(tile2)
        st.image(tile)
        
        s2 = st.button("CLICK TO ENTER",key='2')
        if s2:
            switch_page("northsea")
        df_3_temp = df_3   
        df_3_temp = df_3_temp[df_3_temp['date']==date_selectbox]
        df_3_temp = df_3_temp[df_3_temp['region_name']=='NORTH SEA']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        st.text(south_east_asia_write)
    with col4:
        st.image(north_image_img)
    with col5:
        st.image(tile2)
        st.image(tile)
    
    

with st.container():
    col1,col2,col3,col4,col5,col6 = st.columns([8,2.5,2.5,2.5,4.5,2.5])
    with col6:
        st.image(tile2)
        st.image(tile)
    with col5:
        st.image(india)
    with col3:
        st.image(tile2)
        st.image(tile)
    with col2:
        st.image(tile2)
        st.image(tile)
    with col4:
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        
        s7 = st.button("CLICK TO ENTER",key='8')
        if s7:
            if 'date_value' not in st.session_state:
                st.session_state['date_value'] = date_selectbox
            switch_page("indiarigs")
        df_3_temp = df_3   
        df_3_temp = df_3_temp[df_3_temp['date']==date_selectbox]
        df_3_temp = df_3_temp[df_3_temp['region_name']=='INDIA']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        st.text(south_east_asia_write)
    with col1:
        st.write("--------------------------")
        st.header("REGION - DATA")
        st.write("--------------------------")

    

with st.container():
    col1,col2,col3,col4,col5,col6 = st.columns([2.5,5,2.5,5,2.5,5.5])
    #with col3:
        #st.image(north_image_img)
        #s1 = st.button("ENTER THE REGION",key='1')
    with col1:
        
        s1 = st.button("CLICK TO ENTER",key='4')
        st.image(tile)
        
        df_3_temp = df_3   
        df_3_temp = df_3_temp[df_3_temp['date']==date_selectbox]
        df_3_temp = df_3_temp[df_3_temp['region_name']=='MENAM']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        st.text(south_east_asia_write)
        #st.image(tile)
    with col2:
        st.image(menam)
    with col3:
        
        s1 = st.button("CLICK TO ENTER",key='7')
        if s1:
            switch_page("westafrica")
        st.image(tile)
        
        df_3_temp = df_3   
        df_3_temp = df_3_temp[df_3_temp['date']==date_selectbox]
        df_3_temp = df_3_temp[df_3_temp['region_name']=='WEST AFRICA']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        st.text(south_east_asia_write)
        
    with col4:
        st.image(west_africa)
    with col5:
        #st.image(tile2)
        
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        #st.text("")
        #st.text("")
        st.image(tile)

