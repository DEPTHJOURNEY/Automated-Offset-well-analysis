
import streamlit as st
import time
from PIL import Image
st.set_page_config(layout='centered')
img_path = "https://github.com/JVJayarah3/Automated-Offset-well-analysis/blob/main/oil%20rig1.jpg"
from streamlit_extras.switch_page_button import switch_page
ind_user_list = ["user_1",'user_2',"user_3"]
ind_pass_list = ["user_1","user_2","user_3"]

import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local(img_path)    
st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)

st.title("LOGIN CREDENTIALS")
st.title("")
with st.container():
    col2,col3=  st.columns(2)
    with col2:
        username = st.text_input("USERNAME")
with st.container():
    col2,col3 = st.columns(2)
    with col2:
        password = st.text_input('PASSWORD',type='password')
with st.container():
    col1,col2,col3 = st.columns(3)
    with col2:
        login_button = st.button('LOGIN')
if login_button:
    if username == "admin" and password == "abc@123":
        st.write('LOGGING IN .....')
        with st.spinner("LOADING..."):
            time.sleep(2)
        
        switch_page("test")
        
        
        
        #region_value = "test"
        #switch_page("Rigregions")
        
    else:
        st.write('INCORRECT USERNAME/PASSWORD')
