# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 16:50:36 2023

@author: Jayaraj
"""

import streamlit as st
import time
from PIL import Image
import base64
from streamlit_extras.switch_page_button import switch_page
st.set_page_config(layout='wide')
import pandas as pd

path_1 = "F:/iadc-deep shah/IADC-LAST WELL/SHOWCASE/IADC_WELL_RPT_test.xlsx"
path_2 = "F:/iadc-deep shah/IADC-LAST WELL/SHOWCASE/IADC_WELL_RPT_rig_color.xlsx"
path_3 = "F:/iadc-deep shah/IADC-LAST WELL/SHOWCASE/IADC_WELL_RPT_reg_color.xlsx"
df_1 =  pd.read_excel(path_1)
df_2 =  pd.read_excel(path_2)
df_3 =  pd.read_excel(path_3)

st.write(st.session_state['date_value'])
st.write(st.session_state['rig_value'])

selected_date = st.session_state['date_value']
selected_rig = st.session_state['rig_value']

col1,col2 = st.columns([5,1])
shelf_logo = Image.open("F:/iadc-deep shah/shelf_icon.png")
with col1:
    st.title("SUMMARY")
with col2:
    st.image(shelf_logo)
    home_button = st.button("HOME")
    if home_button:
        switch_page("test")
    
col1,col2 = st.columns(2)
with col1:
    st.write("----------------------")
with col2:
    st.write("----------------------")
   
col1,col2,col3,col4,col5,col6 = st.columns(6)
with col1:
    st.write("DESIGN")
with col2:
    st.write("MAX DRILLING DEPTH")
with col3:
    st.write("LOCATION")
with col4:
    st.write("CLIENT")
with col5:
    st.write("MAX WATER DEPTH")
with col6:
    st.write("MAX ACCOMODATION")

col1,col2 = st.columns(2)
with col1:
    st.write("----------------------")
with col2:
    st.write("----------------------")
change_data = st.button("CHANGE DATA")
if change_data:
    switch_page("mainsheet")
df_temp = df_1
df_temp = df_temp[df_temp['date']==selected_date ]
df_temp = df_temp[df_temp['rig_no']==selected_rig]
df_show = pd.DataFrame()
df_show['Time_count'] = df_temp['Time_count']
df_show['IADC_DESC'] = df_temp['IADC_DESC']
df_show['activity'] = df_temp['activity']

hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)
st.table(df_show)
