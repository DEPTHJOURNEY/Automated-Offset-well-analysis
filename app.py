import streamlit as st
import pandas as pd
import openpyxl
import yagmail



st.title("AUTOMATED OFFSET WELL ANALYSIS")

def main():
    result = st.file_uploader("Upload", type="pdf",accept_multiple_files=True)
    result1 = st.button("ANALYSE")
    if result1:
        st.header("PROCESSING")
        st.text("It may take couple of minutes")
        for r in result:
            st.text(str(r))
        st.text("done")
main()

   
       
