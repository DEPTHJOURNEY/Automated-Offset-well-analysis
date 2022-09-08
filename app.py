import pandas as pd
import sys
import streamlit as st

st.title("AUTOMATED OFFSET WELL ANALYSIS")
def main():
result1 = st.button("ANALYSE")
    if result1:
        st.header("PROCESSING")
        st.text("It may take couple of minutes")
        df = pd.DataFrame()
        df['NAME'] = [1,2,3,4,5]
        df.to_excel("https://github.com/JVJayarah3/Automated-Offset-well-analysis/test.xlsx")
main()       
