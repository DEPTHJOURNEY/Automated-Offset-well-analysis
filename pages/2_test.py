import streamlit as st
import streamlit as st
import time
from streamlit_card import card
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

df_3['date'] = pd.to_datetime(df_3['date']).dt.date
df_3  = df_3.sort_values(by='date',ascending=False)
last_date = df_3['date'].iloc[-1]
print(last_date)

#st.image("https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/shelf drilling logo.png?raw=true")

date_select = df_3['date'].unique()
df_3['date'] = df_3['date'].astype(str)
shelf_logo = "https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/shelf drilling logo.png?raw=true"
north_image_img = "https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/region/north_sea3.jpg?raw=true"
south_east_asia = "https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/region/south_east_asia3.jpg?raw=true"
india = "https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/region/india.jpg?raw=true"
india2 = "https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/region/india2.jpg?raw=true"
india4 = "https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/region/india4.jpg?raw=true"
west_africa = "https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/region/WESTAFRICA2.jpg?raw=true"
menam = "https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/region/MENAM2.jpg?raw=true"
blank = "https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/region/blank.jpg?raw=true"
tile = "https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/region/tile2.jpg?raw=true"
tile2 = "https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/region/tile3.jpg?raw=true"
yellow = "https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/region/yellow.JPG?raw=true"
red = "https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/region/red.JPG?raw=true"
white = "https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/region/white.JPG?raw=true"
green = "https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/region/green.JPG?raw=true"

with st.container():
    col1,col2,col3,col4,col5,col6 =st.columns([6,5,2,5,2.5,2.5])
    with col6:
        st.image(shelf_logo)
    with col5:
        date_selectbox = st.selectbox("DATE",df_3['date'].unique())
    with col1:
        st.header("REGION - DATA")

with st.container():
    col1,col2,col3 = st.columns(3)
    #with col3:
        #st.image(north_image_img)
        #s1 = st.button("ENTER THE REGION",key='1')
    with col1:
        df_3_temp = df_3   
        df_3_temp = df_3_temp[df_3_temp['date']==date_selectbox]
        df_3_temp = df_3_temp[df_3_temp['region_name']=='SOUTH EAST ASIA']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        if south_east_asia_write == "YELLOW":  
            card_color = yellow
        elif south_east_asia_write == "WHITE":  
            card_color = green
        elif south_east_asia_write == "RED":  
            card_color = red
        else:
            card_color = white
        s1 = card(
            title="SOUTH EAST ASIA RIGS",
            text="",
            image = card_color
        )
        
        if s1:
            if 'date_value' not in st.session_state:
                st.session_state['date_value'] = date_selectbox
            
            switch_page("southeastasia")    
    with col2:
        df_3_temp = df_3   
        df_3_temp = df_3_temp[df_3_temp['date']==date_selectbox]
        df_3_temp = df_3_temp[df_3_temp['region_name']=='NORTH SEA']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        if south_east_asia_write == "YELLOW":  
            card_color = yellow
        elif south_east_asia_write == "WHITE":  
            card_color = green
        elif south_east_asia_write == "RED":  
            card_color = red
        else:
            card_color = white
        s2 = card(
            title="NORTH SEA RIGS",
            text="",
            image = card_color
        )
        if s2:
            if 'date_value' not in st.session_state:
                st.session_state['date_value'] = date_selectbox
            
            switch_page("northsea")
    
    with col3:
        df_3_temp = df_3   
        df_3_temp = df_3_temp[df_3_temp['date']==date_selectbox]
        df_3_temp = df_3_temp[df_3_temp['region_name']=='INDIA']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        if south_east_asia_write == "YELLOW":  
            card_color = yellow
        elif south_east_asia_write == "WHITE":  
            card_color = green
        elif south_east_asia_write == "RED":  
            card_color = red
        else:
            card_color = white
        s3 = card(
            title="INDIA RIGS",
            text="",
            image = card_color
        )
        if s3:
            if 'date_value' not in st.session_state:
                st.session_state['date_value'] = date_selectbox
          
            switch_page("indiarigs")
        
    
    col1,col2,col3 = st.columns(3)
    with col1:
        df_3_temp = df_3   
        df_3_temp = df_3_temp[df_3_temp['date']==date_selectbox]
        df_3_temp = df_3_temp[df_3_temp['region_name']=='MENAM']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        
        if south_east_asia_write == "YELLOW":  
            card_color = yellow
        elif south_east_asia_write == "WHITE":  
            card_color = green
        elif south_east_asia_write == "RED":  
            card_color = red
        else:
            card_color = white
        s4 = card(
            title="MENAM RIGS",
            text="",
            image = card_color
        )
        if s4:
            if 'date_value' not in st.session_state:
                st.session_state['date_value'] = date_selectbox
            
            switch_page("menam")
       
   
    with col2:
        df_3_temp = df_3   
        df_3_temp = df_3_temp[df_3_temp['date']==date_selectbox]
        df_3_temp = df_3_temp[df_3_temp['region_name']=='WEST AFRICA']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        
        if south_east_asia_write == "YELLOW":  
            card_color = yellow
        elif south_east_asia_write == "WHITE":  
            card_color = green
        elif south_east_asia_write == "RED":  
            card_color = red
        else:
            card_color = white
        s5 = card(
             title="WEST AFRICA RIGS",
             text="",
             image = card_color
        )
        if s5:
            if 'date_value' not in st.session_state:
                st.session_state['date_value'] = date_selectbox
            switch_page("westafrica")


