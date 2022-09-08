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
        df.to_excel(test.xlsx)
       
main()

   
       
