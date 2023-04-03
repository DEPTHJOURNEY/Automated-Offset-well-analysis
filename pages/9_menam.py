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
path_1 = "https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/IADC_WELL_RPT_test.xlsx?raw=true"
path_2 = "https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/IADC_WELL_RPT_rig_color.xlsx?raw=true"
path_3 = "https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/IADC_WELL_RPT_reg_color.xlsx?raw=true"
df_1 =  pd.read_excel(path_1)
df_2 =  pd.read_excel(path_2)
df_3 =  pd.read_excel(path_3)


selected_date = st.session_state['date_value']
#del st.session_state['date_value']
#for key in st.session_state.keys():
#    del st.session_state[key]

col1,col2 = st.columns([5,1])
shelf_logo = "https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/shelf drilling logo.png?raw=true"

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
        st.write("HARVEY H WARD")
        st.image("https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/menam/Shelf-Drilling_Harvey-H-Ward-200x140.jpg?raw=true")
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='HHW']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        st.text(south_east_asia_write)
        s1 = st.button("SUMMARY",key='1')
        
        if s1:
            #del st.session_state['date_value']
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = "HHW"
            switch_page('summary')
            
        st.write("TRIDENT-XVI")
        st.image("https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/menam/Shelf-Drilling_Trident-16-200x140.jpg?raw=true")
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='T16']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        st.text(south_east_asia_write)
        s12 = st.button("SUMMARY",key='12')
        if s12:
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = "T16"
            switch_page('summary')
            
        st.write("HIGH ISLAND IV")
        st.image("https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/menam/High-Island-IV-IMG_7103-200x140.jpg?raw=true")
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='HI4']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        st.text(south_east_asia_write)
        s13 = st.button("SUMMARY",key='13')
        if s13:
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = "HI4"
            switch_page('summary')
            
            
    with col2:
        st.write("COMPACT DRILLER")
        st.image("https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/menam/Shelf-Drilling_Compact-Driller-200x140.jpg?raw=true")
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='CMD']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        st.text(south_east_asia_write)
        s2 = st.button("SUMMARY",key='2')
        if s2:
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = "CMD"
        
        st.write("KEY MANHATTAN")
        st.image("https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/menam/Key-Manhattan_1-200x140.jpg?raw=true")
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='KMN']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        st.text(south_east_asia_write)
        s22 = st.button("SUMMARY",key='22')
        if s22:
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = "KMN"
            switch_page('summary')
            
        st.write("RESOURCEFUL")
        st.image("https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/menam/SD-Resourceful-200x140.jpg?raw=true")
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='SDR']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        st.text(south_east_asia_write)
        s23 = st.button("SUMMARY",key='23')
        if s23:
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = "SDR"
            switch_page('summary')
            
    with col3:
        st.write("HIGH ISLAND V")
        st.image("https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/menam/High-Island-V_2-200x140.jpg?raw=true")
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='HI5']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        st.text(south_east_asia_write)
        s3 = st.button("SUMMARY",key='3')
        if s3:
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = "HI5"
            switch_page('summary')
                
        st.write("RIG 141")
        st.image("https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/menam/Shelf-Drilling_Rig-141-200x140.jpg?raw=true")
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='141']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        st.text(south_east_asia_write)
        s32 = st.button("SUMMARY",key='32')
        if s32:
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = "141"
            switch_page('summary')
            
        st.write("ACHEIVER")
        st.image("https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/menam/Shelf-Drilling-Achiever-3-200x140.jpg?raw=true")
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='SDA']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        st.text(south_east_asia_write)
        s33 = st.button("SUMMARY",key='33')
        if s33:
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = "SDA"
            switch_page('summary')
            
    with col4:
        st.write("HIGH ISLAND IX")
        st.image("https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/menam/High-Island-IX_1-200x140.jpg?raw=true")
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='HI9']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        st.text(south_east_asia_write)
        s4 = st.button("SUMMARY",key='4')
        if s4:
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = "HI9"
            switch_page('summary')
        #st.button("SUMMARY   ")
        
        st.write("MAIN PASS IV")
        st.image("https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/menam/Shelf-Drilling_Main-Pass-IV-200x140.jpg?raw=true")
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='MP4']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        st.text(south_east_asia_write)
        s42 = st.button("SUMMARY",key='42')
        if s42:
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = "MP4"
            switch_page('summary')
        
        st.write("VICTORY")
        st.image("https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/menam/SDV-1-200x140.jpg?raw=true")
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='SDV']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        st.text(south_east_asia_write)
        s43 = st.button("SUMMARY",key='43')
        if s43:
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = "SDV"
            switch_page('summary')
        
    with col5:
        st.write("HIGH ISLAND II")
        st.image("https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/menam/HI2-Picture-1-Jun-2015-200x140.jpg?raw=true")
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='HI2']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        st.text(south_east_asia_write)
        s5 = st.button("SUMMARY",key='5')
        if s5:
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = "HI2"
            switch_page('summary')
        #st.button("SUMMARY    ")
        
        st.write("MAIN PASS I")
        st.image("https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/menam/Main-Pass-I-Pic-22016-200x140.jpg?raw=true")
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='MP1']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        st.text(south_east_asia_write)
        s52 = st.button("SUMMARY",key='52')
        if s52:
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = "MP1"
            switch_page('summary')
            
        st.write("ODYSSEY")
        st.image("https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/menam/NHC.jpg?raw=true")
        
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='SDO']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        st.text(south_east_asia_write)
        s53 = st.button("SUMMARY",key='53')
        if s53:
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = "SDO"
            switch_page('summary')
