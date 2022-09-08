import streamlit as st
import pandas as pd
import openpyxl

st.title("AUTOMATED OFFSET WELL ANALYSIS")

def main():
    result1 = st.button("ANALYSE")
    if result1:
        st.header("PROCESSING")
        st.text("It may take couple of minutes")
        df = pd.DataFrame()
        df['Name'] = ['Abel','Bake','cook']
        df.to_excel("https://github.com/JVJayarah3/Automated-Offset-well-analysis/main/test.xlsx")
       
main()

import yagmail 

send_ = input("READY TO SEND - (Y/N) - ")
send_ = send_.upper()
if send_ == "Y":
    content = "Dear Sir, \n\t\t\t Kindly find the attached document. \n\n\n\n Thanks & Regards \n Jayaraj J V"
    subject = "One Report - Jindal Star-"
    subject = subject + str(final_date)
    attachment = savepath+str(final_date)+'_JS.xlsx'
    user = 'jvjayaraj7@gmail.com'
    app_password = 'ceyo luws wsef fagr' # a token for gmail
    to = star_dm
    subject = subject
    content = [content,attachment]
    
    print("SUBJECT : ",subject)
    print("CONTENT : ",content)
    send_ = input("READY TO SEND - (Y/N) - ")
    send_ = send_.upper()
    if send_ == "Y":
        with yagmail.SMTP(user, app_password) as yag:
            yag.send(to, subject, content)
            print('Sent email successfully')
    else:
        print("E-mail not send")     
       
