import streamlit as st
import time
from PIL import Image
import base64
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
st.set_page_config(layout='wide',initial_sidebar_state="collapsed")

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)
path_1 = "https://github.com/JVJayarah3/Automated-Offset-well-analysis/blob/main/IADC_WELL_RPT_test.xlsx?raw=true"
path_2 = "https://github.com/JVJayarah3/Automated-Offset-well-analysis/blob/main/IADC_WELL_RPT_rig_color.xlsx?raw=true"
path_3 = "https://github.com/JVJayarah3/Automated-Offset-well-analysis/blob/main/IADC_WELL_RPT_reg_color.xlsx?raw=true"
df_1 =  pd.read_excel(path_1)
df_2 =  pd.read_excel(path_2)
df_3 =  pd.read_excel(path_3)
selected_date = st.session_state['date_value']

col1,col2 = st.columns([5,1])
shelf_logo = "https://github.com/JVJayarah3/Automated-Offset-well-analysis/blob/main/rig_icon/shelf drilling logo.png?raw=true"
with col1:
    st.header("RIGS JACKED UP IN NORTH SEA REGION")
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
        st.write("FORTRESS")
        st.image("https://github.com/JVJayarah3/Automated-Offset-well-analysis/blob/main/rig_icon/north_sea/At-Southwark-from-GC3-3-200x140.jpg?raw=true")
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='SDF']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        st.text(south_east_asia_write)
        s1 = st.button("SUMMARY",key='1')
        if s1:
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = "SDF"
            switch_page('summary')
        
    
    with col2:
        st.write("WINNER")
        st.image("https://github.com/JVJayarah3/Automated-Offset-well-analysis/blob/main/rig_icon/north_sea/Noble-Lloyd-Noble-1-Copy-200x140.jpg?raw=true")
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='SDW']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        st.text(south_east_asia_write)
        s2 = st.button("SUMMARY",key='2')
        if s2:
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = "SDW"
            switch_page('summary')
        
       
        
    with col3:
        st.write("PERSEVERANCE")
        st.image("https://github.com/JVJayarah3/Automated-Offset-well-analysis/blob/main/rig_icon/north_sea/SamHartley-A-20x30-200x140.jpg?raw=true")
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='SDP']
        #df_3_temp = df_3_temp[df_3_temp['rig_no']=='AD-1']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        st.text(south_east_asia_write)
        s3 = st.button("SUMMARY",key='3')
        if s3:
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = "SDP"
            switch_page('summary')
        
        
        
    with col4:
        st.write("BARSK")
        st.image("https://github.com/JVJayarah3/Automated-Offset-well-analysis/blob/main/rig_icon/north_sea/SamTurner-Jul2019-3-200x140.jpg?raw=true")
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='SDB']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        st.text(south_east_asia_write)
        s4 = st.button("SUMMARY",key='4')
        if s4:
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = "SDB"
            switch_page('summary')
