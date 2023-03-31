# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 13:47:10 2023

@author: Jayaraj
"""

import streamlit as st
import time
from PIL import Image
import base64
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
st.set_page_config(layout='wide')
list_1 = ["T1","T2","T3"]
path_1 = "F:/iadc-deep shah/IADC-LAST WELL/SHOWCASE/IADC_WELL_RPT_test.xlsx"
path_2 = "F:/iadc-deep shah/IADC-LAST WELL/SHOWCASE/IADC_WELL_RPT_rig_color.xlsx"
path_3 = "F:/iadc-deep shah/IADC-LAST WELL/SHOWCASE/IADC_WELL_RPT_reg_color.xlsx"

df_1 =  pd.read_excel(path_1)
df_2 =  pd.read_excel(path_2)
df_3 =  pd.read_excel(path_3)

col1,col2 = st.columns([5,1])
shelf_logo = Image.open("F:/iadc-deep shah/shelf_icon.png")
with col1:
    st.header("MASTERSHEET")
with col2:
    home_button = st.button("HOME")
    if home_button:
        switch_page("test")
    st.image(shelf_logo)

col1,col2,col3,col4,col5,col6,col7,col8 = st.columns([3,3,3,3,3,3,2,2])
with col1:
    df_temp = df_1
    reg = st.selectbox("REGION",df_temp['region_name'].unique())
    df_temp['region_name'] = reg
with col2:
    rig = st.selectbox("RIG",df_temp['rig_name'].unique())
    df_temp['rig_name'] = rig
with col3:
    well = st.selectbox("WELL NO",df_temp['well_name'].unique())
    df_temp['well_name'] = well
with col4:
    prob = st.selectbox("PROBLEMS",df_temp['IADC_DESC'].unique())
    df_temp['IADC_DESC']['rig_name'] = prob
with col5:
    date = st.selectbox("DATE",df_temp['date'].unique())
    
with col6:
    month = st.selectbox("MONTH",df_temp['month_wise'].unique())
with col7:
    date = st.button("DATE")
with col8:
    month = st.button("MONTH")
col1,col2 = st.columns(2)
with col1:
    st.write("----------------------")
with col2:
    st.write("----------------------")


