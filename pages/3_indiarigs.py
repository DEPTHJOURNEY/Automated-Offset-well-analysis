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



selected_date = st.session_state['date_value']
#del st.session_state['date_value']
#for key in st.session_state.keys():
#    del st.session_state[key]

col1,col2 = st.columns([5,1])
shelf_logo = Image.open("F:/iadc-deep shah/shelf_icon.png")

with col1:
    st.header("RIGS JACKED UP IN INDIA REGION")
    st.write("SELECTED DATE - "+selected_date)
with col2:
    st.image(shelf_logo)
    home = st.button("HOME")
    if home:
        for key in st.session_state.keys():
            del st.session_state[key]
        switch_page("test")
with st.container():
    #col1,col2,col3,col4,col5,col6,col7,col8,col9,col10 = st.columns(10)
    
    #with col1:
    col1,col2,col3,col4,col5 = st.columns(5)
    
    with col1:
        st.write("RON TAPPMEYER")
        st.image(Image.open("https://github.com/JVJayarah3/Automated-Offset-well-analysis/blob/main/rig_icon/india/RTP-MKT.jpg?raw=true"))
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='RTP']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        st.text(south_east_asia_write)
        s1 = st.button("SUMMARY",key='1')
        
        if s1:
            #del st.session_state['date_value']
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = "RTP"
            switch_page('summary')
            
        st.write("PARAMESHWARA")
        st.image(Image.open("https://github.com/JVJayarah3/Automated-Offset-well-analysis/blob/main/rig_icon/india/Shelf-Drilling-parameshwara.jpg?raw=true"))
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='PSW']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        st.text(south_east_asia_write)
        s12 = st.button("SUMMARY",key='12')
        if s12:
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = "PSW"
            switch_page('summary')
    with col2:
        st.write("THORNTON")
        st.image(Image.open("https://github.com/JVJayarah3/Automated-Offset-well-analysis/blob/main/rig_icon/india/Shelf-Drilling_CE-Thornton-.jpg?raw=true"))
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='CET']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        st.text(south_east_asia_write)
        s2 = st.button("SUMMARY",key='2')
        if s2:
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = "CET"
        
        st.write("J T ANGEL")
        st.image(Image.open("https://github.com/JVJayarah3/Automated-Offset-well-analysis/blob/main/rig_icon/india/SJ-jackup-J-T-Angel.jpg?raw=true"))
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        st.text(south_east_asia_write)
        s22 = st.button("SUMMARY",key='22')
        if s22:
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = ""
            switch_page('summary')
    with col3:
        st.write("FG-MCCLINTOCK")
        st.image(Image.open("https://github.com/JVJayarah3/Automated-Offset-well-analysis/blob/main/rig_icon/india/Shelf-Drilling_FG-McClintock-..jpg?raw=true"))
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='FGM']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        st.text(south_east_asia_write)
        s3 = st.button("SUMMARY",key='3')
        if s3:
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = "FGM"
            switch_page('summary')
                
        st.write("TRIDENT-II")
        st.image(Image.open("https://github.com/JVJayarah3/Automated-Offset-well-analysis/blob/main/rig_icon/india/Trident-II_.jpg?raw=true"))
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='T02']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        st.text(south_east_asia_write)
        s32 = st.button("SUMMARY",key='32')
        if s32:
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = "T02"
            switch_page('summary')
    with col4:
        st.write("TRIDENT-XII")
        st.image(Image.open("https://github.com/JVJayarah3/Automated-Offset-well-analysis/blob/main/rig_icon/india/Shelf-Drilling_Trident-XII_.jpg?raw=true"))
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='T12']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        st.text(south_east_asia_write)
        s4 = st.button("SUMMARY",key='4')
        if s4:
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = ""
            switch_page('summary')
        #st.button("SUMMARY   ")
    with col5:
        st.write("KEY SINGAPORE")
        st.image(Image.open("https://github.com/JVJayarah3/Automated-Offset-well-analysis/blob/main/rig_icon/india/Shelf-Drilling-key singapore.jpg?raw=true"))
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='KSN']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        st.text(south_east_asia_write)
        s5 = st.button("SUMMARY",key='5')
        if s5:
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = ""
            switch_page('summary')
        #st.button("SUMMARY    ")
