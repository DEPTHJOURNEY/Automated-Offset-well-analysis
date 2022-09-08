import streamlit as st
import pandas as pd

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
       
       
