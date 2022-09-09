import streamlit as st
import pandas as pd
import openpyxl
import PyPDF2



st.title("AUTOMATED OFFSET WELL ANALYSIS")

def main():
    result = st.file_uploader("Upload", type="pdf",accept_multiple_files=True)
    result1 = st.button("ANALYSE")
    text = ""
    if result1:
        st.header("PROCESSING")
        st.text("It may take couple of minutes")
        pdf_file_obj = []
        for r in result:
            st.text(str(r))
            pdf_file_obj.append(r)
            #print(x)
            #print(pdf_file_obj)
            
            for x in pdf_file_obj:
                pdf_reader = PyPDF2.PdfFileReader(x)
                for pagenum in range(pdf_reader.numPages):
                    pageobj = pdf_reader.getPage(pagenum)
                    text += pageobj.extractText()
                    #print(text)
                    #text= text.replace("\n"," ")
                    #print(text)
                    text= text.replace("\n"," ")
                    text1 = text
        st.text("done")
        st.text(text1)
main()

   
       
