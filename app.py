import streamlit as st
import pandas as pd
import openpyxl
import yagmail 

st.title("AUTOMATED OFFSET WELL ANALYSIS")

def main():
    result1 = st.button("ANALYSE")
    if result1:
        st.header("PROCESSING")
        st.text("It may take couple of minutes")
        df = pd.DataFrame()
        df['Name'] = ['Abel','Bake','cook']
        content = "Dear Sir, \n\t\t\t Kindly find the attached document. \n\n\n\n Thanks & Regards \n Jayaraj J V"
        subject = "test-onlibe cloud"
        subject = subject 
        user = 'jvjayaraj7@gmail.com'
        app_password = 'ceyo luws wsef fagr' # a token for gmail
        to = "jvjayaraj4@gmail.com"
        with yagmail.SMTP(user, app_password) as yag:
            yag.send(to, subject, content)
        
       
main()

   
       
