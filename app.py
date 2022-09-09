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
            if r.endswith('.pdf'):
                onlypdfs.append(r)
        
        for x in onlypdfs:
            pdf_file_obj =  x
            #print(x)
            #print(pdf_file_obj)
            pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
            text = ""
            for pagenum in range(pdf_reader.numPages):
                pageobj = pdf_reader.getPage(pagenum)
                text += pageobj.extractText()
                #print(text)
                #text= text.replace("\n"," ")
                #print(text)
                text= text.replace("\n"," ")
                text1 = str(text)
        st.text("done")
        st.text(text1)
main()

   
       
