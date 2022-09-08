





import streamlit as st
import os
from PIL import Image

import os

pathd = ("C:/Users/Jayaraj/Desktop/SOFTWARE TEST/INPUT")
for f in os.listdir(pathd):
   os.remove(os.path.join(pathd,f))
   
pathd2 = ("C:/Users/Jayaraj/Desktop/SOFTWARE SHOWCASE/INPUT")
for f in os.listdir(pathd2):
   os.remove(os.path.join(pathd2,f))

st.title("AUTOMATED OFFSET WELL ANALYSIS")
st.header("UPLOAD DOR'S HERE")
#file = st.file_uploader("upload the pdf's",type=['pdf'])

def save_uploaded_file(uploadedfile):
  with open(os.path.join("C:/Users/Jayaraj/Desktop/SOFTWARE SHOWCASE/INPUT",uploadedfile.name),"wb") as f:
     f.write(uploadedfile.getbuffer())
     
  #with open(uploadedfile, "wb") as f:
   #   f.write(uploadedfile.getbuffer())
  
def load_image(image_file):
    img = Image.open(image_file)
    return img





def main():
    
    
    result = st.file_uploader("Upload", type="pdf",accept_multiple_files=True)
    result1 = st.button("ANALYSE")
    if result1:
        st.header("PROCESSING")
        st.text("It may take couple of minutes")
        for r in result:
            save_uploaded_file(r)
    


#file = st.file_uploader("upload the pdf's",type=['pdf'])










        import shutil
        import os
        
        source_folder = 'C:/Users/Jayaraj/Desktop/SOFTWARE SHOWCASE/INPUT'
        destination_folder = 'C:/Users/Jayaraj/Desktop/SOFTWARE TEST/INPUT'
        extension = ".pdf"
        for folders, subfolders,filenames in os.walk(source_folder):
            for filename in filenames:
                if filename.endswith('{}'.format(extension)):
                    shutil.copy(os.path.join(folders,filename), destination_folder)
        
        
        
        
        
        
        import PyPDF2
        import io
        from os import listdir
        from os.path import isfile, join
        
        mypath1 = "C:/Users/Jayaraj/Desktop/SOFTWARE TEST/RESULT/"
        
        mypath = "C:/Users/Jayaraj/Desktop/SOFTWARE TEST/INPUT/" 
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        
        onlypdfs = []
        
        for f in onlyfiles:
            if f.endswith('.pdf'):
                onlypdfs.append(f)
        
        for x in onlypdfs:
            pdf_file_obj = mypath + x
            #print(x)
            print(pdf_file_obj)
            pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
            text = ""
            for pagenum in range(pdf_reader.numPages):
                pageobj = pdf_reader.getPage(pagenum)
                text += pageobj.extractText()
                #print(text)
                #text= text.replace("\n"," ")
                #print(text)
                text= text.replace("\n"," ")
                with io.open(mypath+x[0:-4]+".txt", "w", encoding="utf-8") as f:
                    f.write(text)
                
                
           
        import re
        import pandas as pd
        import sys
        import os
        import glob
        
        # Loading all required methods
        
        def xl_to_desk(filename, df):
            file = filename
            df.to_excel("D:/python_bounce_pad/"+file+".xlsx")
            
            
        
        
        
        # reading raw file
        
        #mypath = "D:/jayaraj/pdf/pdf1/"
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        
        onlytxts = []
        
        for f in onlyfiles:
            if f.endswith('.txt'):
                onlytxts.append(f)
        
        #file_name = mypath+"01 SP-295_SA-0772_MOBILIZATION DOR_27-12-2017.txt"
        
        #file_name    
        #raw = open(file_name).read()
        
        #
        
        
        def conver_raw_txt_rqrd_format241(mypath):
            
            onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
            onlytxts = []
        
            for f in onlyfiles:
                if f.endswith('.txt'):
                    onlytxts.append(f)
            #OKOK      
            #filename = filename
            #raw = open(filename).read()
            #raw = open(file_name, encoding='utf8').read()
            # removing empty lines 
            data = pd.DataFrame()
            
            for i in onlytxts:
                p1 = 0
                p2 = 0
                filename = mypath + i
                raw = open(filename, encoding='utf8').read()
                
                lines = raw.split("\n")
                non_empty_lines = [line for line in lines if line.strip() != ""]
                text = ""
                
                for line in non_empty_lines:
                    text += line + "\n"
                    
                # removing commas in between numericals and equal signs and double spaces
                text = text.replace(',', '')
                text = text.replace('=', '')
                text = text.replace('(in)','')
                text = text.replace('Set MD (ft)', 'Set MD')
                #text = text.replace('Casing Last Size (in)', 'Casing Last Size')
                text = text.replace(" - ", '\n')
                text = re.sub(' +', ' ', text)
                x = []
                for m in re.findall('24 Hours Summary(.*?)24 Hours Forecast', text):
                    x.append(m)
                    data = data.append(x)
            return data
            
        def conver_raw_txt_rqrd_format242(mypath):
            
            onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
            onlytxts = []
        
            for f in onlyfiles:
                if f.endswith('.txt'):
                    onlytxts.append(f)
            #OKOK      
            #filename = filename
            #raw = open(filename).read()
            #raw = open(file_name, encoding='utf8').read()
            # removing empty lines 
            datacs = pd.DataFrame()
            for i in onlytxts:
                p1 = 0
                p2 = 0
                filename = mypath + i
                raw = open(filename, encoding='utf8').read()
                
                lines = raw.split("\n")
                non_empty_lines = [line for line in lines if line.strip() != ""]
                text = ""
                
                for line in non_empty_lines:
                    text += line + "\n"
                    
                # removing commas in between numericals and equal signs and double spaces
                text = text.replace(',', '')
                text = text.replace('=', '')
                text = text.replace('(in)','')
                text = text.replace('Set MD (ft)', 'Set MD')
                #text = text.replace('Casing Last Size (in)', 'Casing Last Size')
                text = text.replace(" - ", '\n')
                text = re.sub(' +', ' ', text)
                x = []
                for r in re.findall('Casing Last Size(.*?)Set MD', text):
                    x.append(r)
                    datacs =datacs.append(x)
            return datacs
        
        def conver_raw_txt_rqrd_format243(mypath):
            
            onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
            onlytxts = []
        
            for f in onlyfiles:
                if f.endswith('.txt'):
                    onlytxts.append(f)
            #OKOK      
            #filename = filename
            #raw = open(filename).read()
            #raw = open(file_name, encoding='utf8').read()
            # removing empty lines 
            datacs = pd.DataFrame()
            
            for i in onlytxts:
                p1 = 0
                p2 = 0
                filename = mypath + i
                raw = open(filename, encoding='utf8').read()
                
                lines = raw.split("\n")
                non_empty_lines = [line for line in lines if line.strip() != ""]
                text = ""
                
                for line in non_empty_lines:
                    text += line + "\n"
                    
                # removing commas in between numericals and equal signs and double spaces
                text = text.replace(',', '')
                text = text.replace('=', '')
                text = text.replace('(in)','')
                text = text.replace('Set MD (ft)', 'Set MD')
                #text = text.replace('Casing Last Size (in)', 'Casing Last Size')
                text = text.replace(" - ", '\n')
                text = re.sub(' +', ' ', text)
                x = []
                for r in re.findall('Set MD(.*?)Next Size', text):
                    x.append(r)
                    datacs =datacs.append(x)
            return datacs
        
        
        
        
        
            
        data = conver_raw_txt_rqrd_format241(mypath)
        data1 = conver_raw_txt_rqrd_format242(mypath)
        data2 = conver_raw_txt_rqrd_format243(mypath)
        
        data = data.rename(columns = {0:"Summary"})
        data1 = data1.rename(columns = {0:"csg_size"})
        data2 = data2.rename(columns = {0:"csd"})
        
        
        dat=pd.concat([data,data1,data2],axis=1)
        pd.set_option('colheader_justify', 'left')
        raw_output_filename = mypath1 + '24hrssummary.xlsx'
        raw_output_filename1 = mypath1 + '24hrssummary'
        dat.to_excel(raw_output_filename, sheet_name='24hrs summary',index=False)
        
        
        import sys
        from PIL import Image
        from win32com.client import Dispatch
        import pandas as pd
        import numpy as np
        import dataframe_image as dfi
        
        
        dfil = dat[['Summary']]
        dfil.set_index("Summary",inplace = True)
        dfil_styled = dfil #adding a gradient based on values in cell
        dfi.export(dfil_styled,mypath1+"Summary.png")

        
        
        
        
        import PyPDF2
        import io
        from os import listdir
        from os.path import isfile, join
        
        mypath1 = "C:/Users/Jayaraj/Desktop/SOFTWARE TEST/RESULT/"
        
        mypath = "C:/Users/Jayaraj/Desktop/SOFTWARE TEST/INPUT/" 
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        
        onlypdfs = []
        
        for f in onlyfiles:
            if f.endswith('.pdf'):
                onlypdfs.append(f)
        
        for x in onlypdfs:
            pdf_file_obj = mypath + x
            #print(x)
            print(pdf_file_obj)
            pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
            text = ""
            for pagenum in range(pdf_reader.numPages):
                pageobj = pdf_reader.getPage(pagenum)
                text += pageobj.extractText()
                #print(text)
                #text= text.replace("\n"," ")
                #print(text)
                text= text.replace("\n"," ")
                with io.open(mypath+x[0:-4]+".txt", "w", encoding="utf-8") as f:
                    f.write(text)
                
                
           
        import re
        import pandas as pd
        import sys
        import os
        import glob
        
        # Loading all required methods
        
        def xl_to_desk(filename, df):
            file = filename
            df.to_excel("D:/python_bounce_pad/"+file+".xlsx")
            
            
        
        # method to extract depth start    
        def depth_start(t):
            return re.findall('^[0-9][0-9]:[0-9][0-9]\s[0-9][0-9]:[0-9][0-9]\s[0-9]:[0-9][0-9].([0-9.]+)', t)
        
        # method to extract depth end
        def depth_end(t):
            return re.findall('^[0-9][0-9]:[0-9][0-9]\s[0-9][0-9]:[0-9][0-9]\s[0-9]:[0-9][0-9]\s[0-9.]+.([0-9.]+)', t)
        
        def hole_section(t):
            return re.findall('^[0-9][0-9]:[0-9][0-9]\s[0-9][0-9]:[0-9][0-9]\s[0-9]:[0-9][0-9]\s[0-9][0-9][0-9.]+\s[0-9][0-9][0-9.]+.([0-9.]+)', t)
        
        def csg_rawsize(t):
            for m in re.finditer('Casing Last Size .([0-9.+]*)', t):
                return (m.group())
        
        def csg_rawdepth(t):
            for m in re.finditer('Set MD .([0-9.+]*)', t):
                return (m.group())
        
                
        
        # Extracting unit of measurement
        def unit_of_measurement(t):
            word_list = t.split()
            return word_list[-1]
        
        
        
        
        # reading raw file
        
        #mypath = "D:/jayaraj/pdf/pdf1/"
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        
        onlytxts = []
        
        for f in onlyfiles:
            if f.endswith('.txt'):
                onlytxts.append(f)
        
        #file_name = mypath+"01 SP-295_SA-0772_MOBILIZATION DOR_27-12-2017.txt"
        
        #file_name    
        #raw = open(file_name).read()
        
        #
        
        
        def conver_raw_txt_rqrd_format(mypath):
            
            onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
            onlytxts = []
        
            for f in onlyfiles:
                if f.endswith('.txt'):
                    onlytxts.append(f)
            #OKOK      
            #filename = filename
            #raw = open(filename).read()
            #raw = open(file_name, encoding='utf8').read()
            # removing empty lines 
            data = pd.DataFrame()
            for i in onlytxts:
                p1 = 0
                p2 = 0
                filename = mypath + i
                raw = open(filename, encoding='utf8').read()
                
                lines = raw.split("\n")
                non_empty_lines = [line for line in lines if line.strip() != ""]
                text = ""
                
                for line in non_empty_lines:
                    text += line + "\n"
                    
                # removing commas in between numericals and equal signs and double spaces
                text = text.replace(',', '')
                text = text.replace('=', '')
                text = text.replace('(in)','')
                text = text.replace('Set MD (ft)', 'Set MD')
                text = text.replace(" - ", '\n')
                text = re.sub(' +', ' ', text)
           
                # Extracting blocks with word loss/losses
                x = []
                for m in re.finditer('[0-9][0-9]:[0-9][0-9]\s[0-9][0-9]:[0-9][0-9]\s[0-9]', text):
                    x.append(m.start())
                    
                data.append(x)
                #return data
                try:
                    
                    p1 = x[0]
                    p2 = x[1]
                    
                    a = 1
                    data1 = []
                    for i in x[1:]:
                        data1.append(text[p1:p2])
                        #print(data1)
                        print("-------------------------GETTING CSD & WELL DATA----------------------------------")
                        p1 = p2
                        a = a+1
                        try:
                            p2 = x[a]
                        except:
                            pass
                    data1 = pd.DataFrame(data1)
                    data1['filename'] = filename
                    #data1 = data1.reset_index()
                    data = pd.concat([data, data1])
                    #data = data.reset_index()
                except:
                    pass
            data = data.reset_index()
            return data
                
            
        data = conver_raw_txt_rqrd_format(mypath)
        #data = conver_raw_txt_rqrd_format(mypath)
        
        
        data = data.rename(columns = {0:"notes"})
        
        Search_for_These_values = ['Casing Last Size (in)'] #creating list
        
        pattern = '|'.join(Search_for_These_values) 
        
        data['csg_siz'] = data['notes'].str.contains(pattern)
        
        # Remove the rows that does not contain the word losses
        
        
        
        data['time_from'] = data.notes.str[0:5]
        
        data['time_to'] = data.notes.str[6:11]
        
        data['duration'] = data.notes.str[12:17]
        
        data['depth_start'] = data.notes.apply(lambda x: depth_start(x))
        data['depth_start']  = data['depth_start'].str.join(', ')
        
        data['depth_end'] = data.notes.apply(lambda x: depth_end(x))
        data['depth_end']  = data['depth_end'].str.join(', ')
        
        data['hole_section'] = data.notes.apply(lambda x: hole_section(x))
        data['hole_section']  = data['hole_section'].str.join(', ')
        
        data['csg_rawsize'] = data.notes.apply(lambda x: csg_rawsize(x))
        data['csg_size'] = data.csg_rawsize.str[16:]
        data['csg_rawdepth'] = data.notes.apply(lambda x: csg_rawdepth(x))
        data['csd'] = data.csg_rawdepth.str[7:]
        #data['fin'] = data.csg_size.apply(lambda col: col.drop_duplicates().reset_index(drop=True))
        
        raw_output_filename = mypath1 + 'raw_OUTPUT(TVD).xlsx'
        raw_output_filename1 = mypath1 + 'raw_OUTPUT(TVD1).xlsx'
        data.to_excel(raw_output_filename, sheet_name='TVD')
        
        data = data.rename(columns = {0:"notes"})
        
        Search_for_These_values1 = ['1','2','3','4','5','6','7','8','9','0'] #creating list
        
        pattern = '|'.join(Search_for_These_values1) 
        
        data['csg_siz1'] = data['csg_size'].str.contains(pattern)
        #c = []
        #for f in data['csg_size']:
         #   if f != None:
          #      c.append(f)
        #data['csg_size'].append(c)
        data = data[data.csg_siz1 == True]
        data.drop_duplicates(subset = 'csg_size', keep = 'last', inplace = True)
        col_list =[ 'csg_size' , 'csd']
        output = data[col_list]
        output_filename1 = mypath1 + 'raw_OUTPUT(TVD1).xlsx'
        data.to_excel(output_filename1, index = None )
        
        
        ## for drawing graph ##
        
        import openpyxl
        from openpyxl import load_workbook
        from openpyxl.worksheet.table import Table, TableStyleInfo
        wb = load_workbook(output_filename1)
        ws = wb.active
        ws.delete_cols(idx = 1 , amount = 11)
        ws.delete_cols(idx =2 , amount = 1 )
        ws.delete_cols(idx = 3, amount = 1)
        
        ws['C1'].value = "c/l"
        ws['D1'].value = 'v/d/h'
        
        ws.cell(row=2, column=3).value = 'C'
        ws.cell(row=2, column=4).value = "V"
        
        ws.cell(row=3, column=3).value = 'L'
        ws.cell(row=3, column=4).value = "V"
        
        ws.cell(row=4,column=3).value = "C"
        ws.cell(row=4,column=4).value = "D"
        
        ws.cell(row=5,column=3).value = "C"
        ws.cell(row=5,column=4).value = "D"
        
        ws.cell(row=6,column=3).value = "C"
        ws.cell(row=6,column=4).value = "D"
        
        ws.cell(row=7,column=3).value = "C"
        ws.cell(row=7,column=4).value = "D"
        
        ws.cell(row=8,column=3).value = "C"
        ws.cell(row=8,column=4).value = "D"
        
        def tabb1():
            ws['F1'].value = 'Casing size'
            ws['G1'].value = 'CSD'
            ws['H1'].value = 'C/L'
            ws['I1'].value = 'V/D/H'
            ws['J1'].value = 'X-axis'
            ws['K1'].value = 'Y-axis'
            
            ws.cell(row=2, column=10).value = 2  
            ws.cell(row=3, column=6).value = ws.cell(row=2, column=1).value
            ws.cell(row=3, column=8).value = ws.cell(row=2,column=3).value
            ws.cell(row=3,column=9).value = ws.cell(row=2,column=4).value
            ws.cell(row=3,column=7).value = ws.cell(row=2, column = 2).value
            ws.cell(row=3,column=11).value = ws.cell(row=3, column=7).value
            ws.cell(row=3, column=10).value = ws.cell(row=2, column=10).value
            
            
            if ws.cell(row=3,column=8).value =='C' :
                ws.cell(row = 2, column= 11).value = 0
            if ws.cell(row=3,column=8).value =='L' :
                ws.cell(row = 2, column= 11).value = ws.cell(row=3,column=7)
            
            
         
            
        
        def tabb2():
            
            
            ws.cell(row=6, column=10).value = int(ws.cell(row=3, column=10).value) + 1
            ws.cell(row=7, column=7).value = ws.cell(row=3,column=2).value
            ws.cell(row=7, column=8).value = ws.cell(row=3,column=3).value
            ws.cell(row=7, column=9).value = ws.cell(row=3,column=4).value
            ws.cell(row=7, column=6).value = ws.cell(row=3, column=1).value
            ws.cell(row=7, column = 11).value = ws.cell(row=7, column=7).value
            ws.cell(row=7, column=10).value = int(ws.cell(row=6, column=10).value)
            
            
            if ws.cell(row=7,column=8).value =='C' :
                ws.cell(row = 6, column= 11).value = 0
            if ws.cell(row=7,column=8).value =='L' :
                ws.cell(row = 6, column= 11).value = ws.cell(row=3,column=7).value
            
           
           
            
        
        def tabb3():
          
                
                
                ws.cell(row=11, column=7).value = ws.cell(row=4,column=2).value
                ws.cell(row=11, column=8).value = ws.cell(row=4, column=3).value
                ws.cell(row=11, column=9).value = ws.cell(row=4, column=4).value
                ws.cell(row=10, column=10).value = int(ws.cell(row=7, column=10).value) + 1
                ws.cell(row=11, column=6).value = ws.cell(row=4, column=1).value
                ws.cell(row=11, column = 11).value = ws.cell(row=11, column=7).value
                ws.cell(row=11, column=10).value = ws.cell(row=10, column=10).value
                
                
                if ws.cell(row=11,column=8).value =='C' :
                    ws.cell(row = 10, column= 11).value = 0
                if ws.cell(row=11,column=8).value =='L' :
                    ws.cell(row = 10, column= 11).value = ws.cell(row=11,column=7)
                
               
               
                
            
        ###
        def tabb4():
            try:
                
                
                ws.cell(row=15, column=7).value = ws.cell(row=5,column=2).value
                ws.cell(row=15, column=8).value = ws.cell(row=5, column=3).value
                ws.cell(row=15, column=9).value = ws.cell(row=5, column=4).value
                ws.cell(row=14, column=10).value = ws.cell(row=10, column=10).value + 1
                ws.cell(row=15, column=6).value = ws.cell(row=5, column=1).value
                ws.cell(row=15, column = 11).value = ws.cell(row=15, column=7).value
                ws.cell(row=15, column=10).value = ws.cell(row=14, column=10).value
                
                
                if ws.cell(row=15,column=8).value =='C' :
                    ws.cell(row = 14, column= 11).value = '0'
                if ws.cell(row=15,column=8).value =='L' :
                    ws.cell(row = 14, column= 11).value = ws.cell(row=15,column=7)
                
               
                
            except:
                pass
        
        def tabb5():
            try:
                
                
                ws.cell(row=19, column=7).value = ws.cell(row=6,column=2).value
                ws.cell(row=19, column=8).value = ws.cell(row=6, column=3).value
                ws.cell(row=19, column=9).value = ws.cell(row=6, column=4).value
                ws.cell(row=18, column=10).value = ws.cell(row=14, column=10).value + 1
                ws.cell(row=19, column=6).value = ws.cell(row=6, column=1).value
                ws.cell(row=19, column = 11).value = ws.cell(row=19, column=7).value
                ws.cell(row=19, column=10).value = ws.cell(row=18, column=10).value
                
                
                if ws.cell(row=19,column=8).value =='C' :
                    ws.cell(row = 18, column= 11).value = '0'
                if ws.cell(row=19,column=8).value =='L' :
                    ws.cell(row = 18, column= 11).value = ws.cell(row=19,column=7)
                
               
                
            except:
                pass
            
        def tabb6():
            try:
                
                
                ws.cell(row=23, column=7).value = ws.cell(row=7,column=2).value
                ws.cell(row=23, column=8).value = ws.cell(row=7, column=3).value
                ws.cell(row=23, column=9).value = ws.cell(row=7, column=4).value
                ws.cell(row=22, column=10).value = ws.cell(row=18, column=10).value + 1
                ws.cell(row=23, column=6).value = ws.cell(row=7, column=1).value
                ws.cell(row=23, column = 11).value = ws.cell(row=23, column=7).value
                ws.cell(row=23, column=10).value = ws.cell(row=22, column=10).value
                
                
                if ws.cell(row=23,column=8).value =='C' :
                    ws.cell(row = 22, column= 11).value = '0'
                if ws.cell(row=23,column=8).value =='L' :
                    ws.cell(row = 22, column= 11).value = ws.cell(row=23,column=7)
                
               
                
            except:
                pass
        
        def tabb7():
            try:
                
                
                ws.cell(row=27, column=7).value = ws.cell(row=8,column=2).value
                ws.cell(row=27, column=8).value = ws.cell(row=8, column=3).value
                ws.cell(row=27, column=9).value = ws.cell(row=8, column=4).value
                ws.cell(row=26, column=10).value = ws.cell(row=22, column=10).value + 1
                ws.cell(row=27, column=6).value = ws.cell(row=8, column=1).value
                ws.cell(row=27, column = 11).value = ws.cell(row=27, column=7).value
                ws.cell(row=27, column=10).value = ws.cell(row=26, column=10).value
                
                
                if ws.cell(row=27,column=8).value =='C' :
                    ws.cell(row = 26, column= 11).value = '0'
                if ws.cell(row=27,column=8).value =='L' :
                    ws.cell(row = 26, column= 11).value = ws.cell(row=27,column=7)
                
               
            except:
                pass
        
        ###
        
        tabb1()
        tabb2()
        tabb3()
        tabb4()
        tabb5()
        tabb6()
        tabb7()
        
        wb.save( filename = mypath1 + 'raw_OUTPUT(TVD-graph).xlsx') 
        
        ## LOSSES
        
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        
        onlypdfs = []
        
        for f in onlyfiles:
            if f.endswith('.pdf'):
                onlypdfs.append(f)
        
        for x in onlypdfs:
            pdf_file_obj = mypath + x
            #print(x)
            print(pdf_file_obj)
            pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
            text = ""
            for pagenum in range(pdf_reader.numPages):
                pageobj = pdf_reader.getPage(pagenum)
                text += pageobj.extractText()
                #print(text)
                #text= text.replace("\n"," ")
                #print(text)
                text= text.replace("\n"," ")
                with io.open(mypath+x[0:-4]+".txt", "w", encoding="utf-8") as f:
                    f.write(text)
                
                
           
        import re
        import pandas as pd
        import sys
        import os
        import glob
        
        # Loading all required methods
        
        def xl_to_desk(filename, df):
            file = filename
            df.to_excel("D:/python_bounce_pad/"+file+".xlsx")
            
            
        
        # method to extract depth start    
        def depth_start(t):
            return re.findall('^[0-9][0-9]:[0-9][0-9]\s[0-9][0-9]:[0-9][0-9]\s[0-9]:[0-9][0-9].([0-9.]+)', t)
        
        # method to extract depth end
        def depth_end(t):
            return re.findall('^[0-9][0-9]:[0-9][0-9]\s[0-9][0-9]:[0-9][0-9]\s[0-9]:[0-9][0-9]\s[0-9.]+.([0-9.]+)', t)
        
        # method to extract losses (from the word losses to end of that line)
        def losses_raw(t):
            for m in re.finditer('losses.*([0-9.]+)', t):
                return (m.group())
        
        # extrace losses rate or losses 
        def losses(t):
            return re.findall('losses.([\d+-?.]+)', t)
            
        def losses1(t):
            try:
                return re.findall('losses\srate:.([\d+-?.]+)', t)
            except:   
                pass
        
        # Extracting unit of measurement
        def unit_of_measurement(t):
            word_list = t.split()
            return word_list[-1]
        
        
        
        
        # reading raw file
        
        #mypath = "D:/jayaraj/pdf/pdf1/"
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        
        onlytxts = []
        
        for f in onlyfiles:
            if f.endswith('.txt'):
                onlytxts.append(f)
        
        #file_name = mypath+"01 SP-295_SA-0772_MOBILIZATION DOR_27-12-2017.txt"
        
        #file_name    
        #raw = open(file_name).read()
        
        #
        
        
        def conver_raw_txt_rqrd_format(mypath):
            
            onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
            onlytxts = []
        
            for f in onlyfiles:
                if f.endswith('.txt'):
                    onlytxts.append(f)
            #OKOK      
            #filename = filename
            #raw = open(filename).read()
            #raw = open(file_name, encoding='utf8').read()
            # removing empty lines 
            data = pd.DataFrame()
            for i in onlytxts:
                p1 = 0
                p2 = 0
                filename = mypath + i
                raw = open(filename, encoding='utf8').read()
                
                lines = raw.split("\n")
                non_empty_lines = [line for line in lines if line.strip() != ""]
                text = ""
                
                for line in non_empty_lines:
                    text += line + "\n"
                    
                # removing commas in between numericals and equal signs and double spaces
                text = text.replace(',', '')
                text = text.replace('=', '')
                text = text.replace(" - ", '\n')
                text = re.sub(' +', ' ', text)
           
                # Extracting blocks with word loss/losses
                x = []
                for m in re.finditer('[0-9][0-9]:[0-9][0-9]\s[0-9][0-9]:[0-9][0-9]\s[0-9]', text):
                    x.append(m.start())
                    
                data.append(x)
                #return data
                try:
                    
                    p1 = x[0]
                    p2 = x[1]
                    
                    a = 1
                    data1 = []
                    for i in x[1:]:
                        data1.append(text[p1:p2])
                        #print(data1)
                        print("-----------------------LOADING LOSSES---------------------------------------")
                        p1 = p2
                        a = a+1
                        try: 
                            p2 = x[a]
                        except:
                            pass
                    data1 = pd.DataFrame(data1)
                    data1['filename'] = filename
                    #data1 = data1.reset_index()
                    data = pd.concat([data, data1])
                    #data = data.reset_index()
                except:
                    pass
            data = data.reset_index()
            return data
                
            
        data = conver_raw_txt_rqrd_format(mypath)
        #data = conver_raw_txt_rqrd_format(mypath)
        
        
        data = data.rename(columns = {0:"notes"})
        
        #data["losses_available"] = data.notes.str.contains('losses')
        
        
        Search_for_These_values = ['losses', 'losses rate'] #creating list
        
        pattern = '|'.join(Search_for_These_values) 
        
        data['losses_available'] = data['notes'].str.contains(pattern)
        
        # Remove the rows that does not contain the word losses
        
        data = data[data.losses_available == True]
        
        data['time_from'] = data.notes.str[0:5]
        
        data['time_to'] = data.notes.str[6:11]
        
        data['duration'] = data.notes.str[12:17]
        
        data['depth_start'] = data.notes.apply(lambda x: depth_start(x))
        data['depth_start']  = data['depth_start'].str.join(', ')
        
        try:
            data['depth_start']  = data['depth_start'].astype(float)
        except:
            pass
        
        data['depth_end'] = data.notes.apply(lambda x: depth_end(x))
        data['depth_end']  = data['depth_end'].str.join(', ')
        try:
            data['depth_end']  = data['depth_end'].astype(float)
        except:
            pass
        
        data['losses_raw'] = data.notes.apply(lambda x: losses_raw(x))
        
        data['dummy_index'] = data.index
        
        Search_for_These_values1 = ['losses', 'losses rate'] #creating list
        
        pattern1 = '|'.join(Search_for_These_values1) 
        
        data['losses_test'] = data['losses_raw'].str.contains(pattern1)
        data = data[data.losses_test == True]
        
        data.loc[data.losses_raw.str.contains('rate'), 'dummy'] = 'Yes'
        
        data1 = data[data.dummy != 'Yes']
        data2 = data[data.dummy == 'Yes']
        data1 = data1.reset_index()
        data2 = data2.reset_index()
        
        data1['loss'] = data1['losses_raw'].apply(lambda x: losses(x))
        
        data2['loss'] = data2.losses_raw.apply(lambda x: losses1(x))
        
        def types(t):
            
                pass
        
        def emptt():
            
                pass
                
        
        data_final = pd.concat([data1, data2])
        
        data_final = data_final.sort_values(by='dummy_index', ascending=True)
        data_final['loss']  = data_final['loss'].str.join(', ')
        
        data_final[['losses_from','losses_to']] = data_final.loss.str.split("-",expand=True,)
        
        try:
            data_final['losses_from'] = data_final.losses_from.astype(float)
        except:
            pass
        
        try:
            data_final['losses_to'] = data_final.losses_to.astype(float)
        except:
            pass
        
        Search_for_These_values2 = ['1','2','3','4','5','6','7','8','9','0']
        pattern2 = '|'.join(Search_for_These_values2) 
        data_final['losses_available1'] = data_final['losses_from'].str.contains(pattern2)
        
        
        
        data_final = data_final[data_final.losses_available1 == True]
        
        data_final['unit_of_measurement'] = data_final.losses_raw.apply(lambda x: unit_of_measurement(x))
        data_final['types'] = data_final.losses_from.apply(lambda x: types(x))
        data_final['emptt'] = data_final.losses_from.apply(lambda x: types(x))
        
        #xl_to_desk("numbre9", data_final)
        
        col_list = ['time_from', 'time_to', 'duration', 'depth_start', 'depth_end',
               'losses_raw', 'losses_from', 'losses_to', 'unit_of_measurement', 'types', 'emptt', 'emptt' , 'emptt', 'emptt' , 'emptt', 'emptt', 'emptt' , 'filename', 'notes']
        
        output = data_final[col_list]
        
        output_filename = mypath1+'raw_OUTPUT(Losses).xlsx'
        
        data_final.to_excel(output_filename)
        
        ## WELL CONTROL
        
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        
        onlypdfs = []
        
        for f in onlyfiles:
            if f.endswith('.pdf'):
                onlypdfs.append(f)
        
        for x in onlypdfs:
            pdf_file_obj = mypath + x
            #print(x)
            print(pdf_file_obj)
            pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
            text = ""
            for pagenum in range(pdf_reader.numPages):
                pageobj = pdf_reader.getPage(pagenum)
                text += pageobj.extractText()
                #print(text)
                #text= text.replace("\n"," ")
                #print(text)
                text= text.replace("\n"," ")
                with io.open(mypath+x[0:-4]+".txt", "w", encoding="utf-8") as f:
                    f.write(text)
                
                
           
        import re
        import pandas as pd
        import sys
        import os
        import glob
        
        # Loading all required methods
        
        def xl_to_desk(filename, df):
            file = filename
            df.to_excel("D:/python_bounce_pad/"+file+".xlsx")
            
            
        
        # method to extract depth start    
        def depth_start(t):
            return re.findall('^[0-9][0-9]:[0-9][0-9]\s[0-9][0-9]:[0-9][0-9]\s[0-9]:[0-9][0-9].([0-9.]+)', t)
        
        # method to extract depth end
        def depth_end(t):
            return re.findall('^[0-9][0-9]:[0-9][0-9]\s[0-9][0-9]:[0-9][0-9]\s[0-9]:[0-9][0-9]\s[0-9.]+.([0-9.]+)', t)
        
        # method to extract losses (from the word losses to end of that line)
        def kick_raw(t):
            for m in re.finditer('flow at.*([0-9.]+)', t):
                return (m.group())
            
        # extrace losses rate or losses 
        def kick(t):
            return re.findall('kill mud.*(ppg+', t)
                    
        def kick1(t):
                for m in re.finditer('(kill mud.*+)', t):
                    return (m.group())  
        
        # Extracting unit of measurement
        def unit_of_measurement(t):
            word_list = t.split()
            return word_list[-1]
        
        
        
        
        # reading raw file
        
        #mypath = "D:/jayaraj/pdf/pdf1/"
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        
        onlytxts = []
        
        for f in onlyfiles:
            if f.endswith('.txt'):
                onlytxts.append(f)
        
        #file_name = mypath+"01 SP-295_SA-0772_MOBILIZATION DOR_27-12-2017.txt"
        
        #file_name    
        #raw = open(file_name).read()
        
        #
        
        
        def conver_raw_txt_rqrd_format(mypath):
            
            onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
            onlytxts = []
        
            for f in onlyfiles:
                if f.endswith('.txt'):
                    onlytxts.append(f)
            #OKOK      
            #filename = filename
            #raw = open(filename).read()
            #raw = open(file_name, encoding='utf8').read()
            # removing empty lines 
            data = pd.DataFrame()
            for i in onlytxts:
                p1 = 0
                p2 = 0
                filename = mypath + i
                raw = open(filename, encoding='utf8').read()
                
                lines = raw.split("\n")
                non_empty_lines = [line for line in lines if line.strip() != ""]
                text = ""
                
                for line in non_empty_lines:
                    text += line + "\n"
                    
                # removing commas in between numericals and equal signs and double spaces
                text = text.replace(',', '')
                text = text.replace('=', '')
                text = text.replace(" - ", '\n')
                text = re.sub(' +', ' ', text)
           
                # Extracting blocks with word loss/losses
                x = []
                for m in re.finditer('[0-9][0-9]:[0-9][0-9]\s[0-9][0-9]:[0-9][0-9]\s[0-9]', text):
                    x.append(m.start())
                    
                data.append(x)
                #return data
                try:
                    
                    p1 = x[0]
                    p2 = x[1]
                    
                    a = 1
                    data1 = []
                    for i in x[1:]:
                        data1.append(text[p1:p2])
                        #print(data1)
                        print("--------------------------LOADING WELL-CONTROL-------------------")
                        p1 = p2
                        a = a+1
                        try:
                            p2 = x[a]
                        except:
                            pass
                    data1 = pd.DataFrame(data1)
                    data1['filename'] = filename
                    #data1 = data1.reset_index()
                    data = pd.concat([data, data1])
                    #data = data.reset_index()
                except:
                    pass
            data = data.reset_index()
            return data
                
            
        data = conver_raw_txt_rqrd_format(mypath)
        #data = conver_raw_txt_rqrd_format(mypath)
        
        
        data = data.rename(columns = {0:"notes"})
        
        Search_for_These_values = ['well flow', 'kick' , 'kill' , 'well control'] #creating list
        
        pattern = '|'.join(Search_for_These_values) 
        
        data['flow_available'] = data['notes'].str.contains(pattern)
        
        # Remove the rows that does not contain the word losses
        
        data = data[data.flow_available == True]
        
        data['time_from'] = data.notes.str[0:5]
        
        data['time_to'] = data.notes.str[6:11]
        
        data['duration'] = data.notes.str[12:17]
        
        data['depth_start'] = data.notes.apply(lambda x: depth_start(x))
        data['depth_start']  = data['depth_start'].str.join(', ')
        
        data['depth_end'] = data.notes.apply(lambda x: depth_end(x))
        data['depth_end']  = data['depth_end'].str.join(', ')
        
        data['kick_raw'] = data.notes.apply(lambda x: kick_raw(x))
        
        
        
        
        raw_output_filename = mypath1 + 'raw_OUTPUT(wellcontrol).xlsx'
        data.to_excel(raw_output_filename)
        
        ## FISH IN HOLE
        
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        
        onlypdfs = []
        
        for f in onlyfiles:
            if f.endswith('.pdf'):
                onlypdfs.append(f)
        
        for x in onlypdfs:
            pdf_file_obj = mypath + x
            #print(x)
            print(pdf_file_obj)
            pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
            text = ""
            for pagenum in range(pdf_reader.numPages):
                pageobj = pdf_reader.getPage(pagenum)
                text += pageobj.extractText()
                #print(text)
                #text= text.replace("\n"," ")
                #print(text)
                text= text.replace("\n"," ")
                with io.open(mypath+x[0:-4]+".txt", "w", encoding="utf-8") as f:
                    f.write(text)
                
                
           
        import re
        import pandas as pd
        import sys
        import os
        import glob
        
        # Loading all required methods
        
        def xl_to_desk(filename, df):
            file = filename
            df.to_excel("D:/python_bounce_pad/"+file+".xlsx")
            
            
        
        # method to extract depth start    
        def depth_start(t):
            return re.findall('^[0-9][0-9]:[0-9][0-9]\s[0-9][0-9]:[0-9][0-9]\s[0-9]:[0-9][0-9].([0-9.]+)', t)
        
        # method to extract depth end
        def depth_end(t):
            return re.findall('^[0-9][0-9]:[0-9][0-9]\s[0-9][0-9]:[0-9][0-9]\s[0-9]:[0-9][0-9]\s[0-9.]+.([0-9.]+)', t)
        
        # method to extract losses (from the word losses to end of that line)
        def fish_raw(t):
            for m in re.finditer('fish', t):
                return (m.group())
            
        # extrace losses rate or losses 
        def fish(t):
            return re.findall('kill mud.*(ppg+', t)
                    
        def kick1(t):
                for m in re.finditer('(kill mud.*+)', t):
                    return (m.group())  
        
        # Extracting unit of measurement
        def unit_of_measurement(t):
            word_list = t.split()
            return word_list[-1]
        
        
        
        
        # reading raw file
        
        #mypath = "D:/jayaraj/pdf/pdf1/"
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        
        onlytxts = []
        
        for f in onlyfiles:
            if f.endswith('.txt'):
                onlytxts.append(f)
        
        #file_name = mypath+"01 SP-295_SA-0772_MOBILIZATION DOR_27-12-2017.txt"
        
        #file_name    
        #raw = open(file_name).read()
        
        #
        
        
        def conver_raw_txt_rqrd_format(mypath):
            
            onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
            onlytxts = []
        
            for f in onlyfiles:
                if f.endswith('.txt'):
                    onlytxts.append(f)
            #OKOK      
            #filename = filename
            #raw = open(filename).read()
            #raw = open(file_name, encoding='utf8').read()
            # removing empty lines 
            data = pd.DataFrame()
            for i in onlytxts:
                p1 = 0
                p2 = 0
                filename = mypath + i
                raw = open(filename, encoding='utf8').read()
                
                lines = raw.split("\n")
                non_empty_lines = [line for line in lines if line.strip() != ""]
                text = ""
                
                for line in non_empty_lines:
                    text += line + "\n"
                    
                # removing commas in between numericals and equal signs and double spaces
                text = text.replace(',', '')
                text = text.replace('=', '')
                text = text.replace(" - ", '\n')
                text = re.sub(' +', ' ', text)
           
                # Extracting blocks with word loss/losses
                x = []
                for m in re.finditer('[0-9][0-9]:[0-9][0-9]\s[0-9][0-9]:[0-9][0-9]\s[0-9]', text):
                    x.append(m.start())
                    
                data.append(x)
                #return data
                try:
                    
                    p1 = x[0]
                    p2 = x[1]
                    
                    a = 1
                    data1 = []
                    for i in x[1:]:
                        data1.append(text[p1:p2])
                        #print(data1)
                        print("--------------------------LOADING--FISH IN HOLE--------------")
                        p1 = p2
                        a = a+1
                        try:
                            p2 = x[a]
                        except:
                            pass
                    data1 = pd.DataFrame(data1)
                    data1['filename'] = filename
                    #data1 = data1.reset_index()
                    data = pd.concat([data, data1])
                    #data = data.reset_index()
                except:
                    pass
            data = data.reset_index()
            return data
                
            
        data = conver_raw_txt_rqrd_format(mypath)
        #data = conver_raw_txt_rqrd_format(mypath)
        
        
        data = data.rename(columns = {0:"notes"})
        
        Search_for_These_values = ['fish', 'left in hole' , 'fishing' , 'L I H' ] #creating list
        
        pattern = '|'.join(Search_for_These_values) 
        
        data['flow_available'] = data['notes'].str.contains(pattern)
        
        # Remove the rows that does not contain the word losses
        
        data = data[data.flow_available == True]
        
        data['time_from'] = data.notes.str[0:5]
        
        data['time_to'] = data.notes.str[6:11]
        
        data['duration'] = data.notes.str[12:17]
        
        data['depth_start'] = data.notes.apply(lambda x: depth_start(x))
        data['depth_start']  = data['depth_start'].str.join(', ')
        
        data['depth_end'] = data.notes.apply(lambda x: depth_end(x))
        data['depth_end']  = data['depth_end'].str.join(', ')
        
        
        
        
        
        
        raw_output_filename = mypath1 + 'raw_OUTPUT(fish).xlsx'
        data.to_excel(raw_output_filename)
        
        
        
        
        # Organising excel
        import openpyxl
        from openpyxl import load_workbook
        #TVD
        wb = load_workbook(mypath1 + "raw_OUTPUT(TVD).xlsx")
        ws = wb.active
        ws.delete_cols(idx = 1 , amount = 5)
        wb.save(mypath1 + "raw_OUTPUT(TVD).xlsx")
        #TVD1
        wb = load_workbook(mypath1 + "raw_OUTPUT(TVD1).xlsx")
        ws = wb.active
        ws.delete_cols(idx = 1 , amount = 5)
        wb.save(mypath1 + "raw_OUTPUT(TVD1).xlsx")
        #LOSSES
        wb = load_workbook(mypath1 + "raw_OUTPUT(Losses).xlsx")
        ws = wb.active
        ws.delete_cols(idx = 1 , amount = 3)
        ws.delete_cols(idx =2 , amount = 2)
        #ws.detele_cols(idx = 8 , amount = 4)
        #ws.delete_cols(idx = 2, amount= 3 )
        wb.save(mypath1 + "raw_OUTPUT(Losses).xlsx")
        #WELL CONTROL
        wb = load_workbook(mypath1 + "raw_OUTPUT(wellcontrol).xlsx")
        ws = wb.active
        ws.delete_cols(idx = 1 , amount = 2)
        ws.delete_cols(idx =2 , amount = 2)
        wb.save(mypath1 + "raw_OUTPUT(wellcontrol).xlsx")
        #fish
        wb = load_workbook(mypath1 + "raw_OUTPUT(fish).xlsx")
        ws = wb.active
        ws.delete_cols(idx = 1 , amount = 2)
        ws.delete_cols(idx =2 , amount = 2)
        wb.save(mypath1 + "raw_OUTPUT(fish).xlsx")
        
        
        
        
        
        import pandas as pd
        import numpy as np
        import os
        import openpyxl
        from openpyxl import load_workbook
        
        ## X-Axis
        
        wb = load_workbook("C:/Users/Jayaraj/Desktop/SOFTWARE TEST/RESULT/raw_OUTPUT(Losses).xlsx")
        ws=wb.active
        for r in ws['J']:
            for w in ws['W']:
                w.value = 1.7
        ws['W1'].value = 'L X axis' 
        wb.save("C:/Users/Jayaraj/Desktop/SOFTWARE TEST/RESULT/raw_OUTPUT(Losses).xlsx")
        
        wb = load_workbook("C:/Users/Jayaraj/Desktop/SOFTWARE TEST/RESULT/raw_OUTPUT(wellcontrol).xlsx")
        ws=wb.active
        for r in ws['I']:
            for w in ws['W']:
                w.value = 1.4
        ws['W1'].value = 'W X axis' 
        wb.save("C:/Users/Jayaraj/Desktop/SOFTWARE TEST/RESULT/raw_OUTPUT(wellcontrol).xlsx")
        
        wb = load_workbook("C:/Users/Jayaraj/Desktop/SOFTWARE TEST/RESULT/raw_OUTPUT(fish).xlsx")
        ws=wb.active
        for r in ws['E']:
            for w in ws['W']:
                w.value = 1.1
        ws['W1'].value = 'F X axis' 
        wb.save("C:/Users/Jayaraj/Desktop/SOFTWARE TEST/RESULT/raw_OUTPUT(fish).xlsx")
        
        wb = load_workbook("C:/Users/Jayaraj/Desktop/SOFTWARE TEST/RESULT/raw_OUTPUT(TVD-graph).xlsx")
        ws=wb.active
        a = 1
        
        for w in ws['E']:
                
            w.value = a
            a = a + 1
        ws['E1'].value = 'S X axis' 
        
        wb.save("C:/Users/Jayaraj/Desktop/SOFTWARE TEST/RESULT/raw_OUTPUT(TVD-graph).xlsx")
        
        
        ## Summary
        
        l = pd.read_excel("C:/Users/Jayaraj/Desktop/SOFTWARE TEST/RESULT/raw_OUTPUT(Losses).xlsx")
        t = pd.read_excel("C:/Users/Jayaraj/Desktop/SOFTWARE TEST/RESULT/raw_OUTPUT(TVD).xlsx")
        tg = pd.read_excel("C:/Users/Jayaraj/Desktop/SOFTWARE TEST/RESULT/raw_OUTPUT(TVD-graph).xlsx")
        w = pd.read_excel("C:/Users/Jayaraj/Desktop/SOFTWARE TEST/RESULT/raw_OUTPUT(wellcontrol).xlsx")
        f = pd.read_excel("C:/Users/Jayaraj/Desktop/SOFTWARE TEST/RESULT/raw_OUTPUT(fish).xlsx")
        
        
        dfl = l[['notes','depth_start','depth_end','time_from','time_to','duration','losses_raw']]
        dfw = w[['notes','depth_start','depth_end','time_from','time_to','duration','kick_raw']]
        dff = f[['notes','depth_start','depth_end','time_from','time_to','duration',]]
        dftg = tg[['csg_size','csd','c/l','v/d/h']]
        dftg1 = tg[['Casing size','CSD','C/L','V/D/H','X-axis','Y-axis']]
        
         
        #dftg = tg[['csg_size','csd','c/l','v/d/h']]
        #dftg = dftg.dropna()
        #dftg1 = tg[['Y-axis','X-axis']]
        #dftg1 = dftg1.dropna()
        #dftg1 = tg[['Y-axis','X-axis']]
        #print(dftg)
        #df = pd.DataFrame([[dftg],[dftg1]])
        #print(dftg)
        #print(dftg1)
        path = "C:/Users/Jayaraj/Desktop/SOFTWARE SHOWCASE/OUTPUT/Summary.xlsx"
        writer = pd.ExcelWriter(path,engine='openpyxl')
        with pd.ExcelWriter(path) as writer:
            #writer.book = load_workbook(path)
            dftg.to_excel(writer, sheet_name= 'CSD', index=False)
            dfl.to_excel(writer, sheet_name= 'losses',index=False)
            dfw.to_excel(writer, sheet_name= 'wellcontroll',index=False)
            dff.to_excel(writer, sheet_name= 'fish',index=False)
        #with pd.ExcelWriter(path1) as writer:
        
            
        import pandas as pd
        import numpy as np
        import os
        import openpyxl
        from openpyxl import load_workbook
        import matplotlib.pyplot as plt
        from matplotlib.offsetbox import OffsetImage, AnnotationBbox
        from matplotlib.cbook import get_sample_data
        import matplotlib.cbook as cbook
        
        
        dfl = l[['depth_start','L X axis']]
        dfw = w[['depth_start','W X axis']]
        dff = f[['depth_start','F X axis']]
        dft = tg[['X-axis','Y-axis','csd','S X axis']]
        
        
        graph, ax = plt.subplots(1)
        xf = (dff[['F X axis']])
        yf = (dff[['depth_start']])
        xc = (dft[['X-axis']])
        yc = (dft[['Y-axis']])
        xw = (dfw[['W X axis']])
        yw = (dfw[['depth_start']])
        x = (dft[['S X axis']])
        xl = (dfl[['L X axis']])
        y = (dft[['csd']])
        yl = (dfl[['depth_start']])
        ax.scatter(xl,yl,marker='X',label = 'Losses',color = 'y')
        ax.scatter(xw,yw,marker='X',label = 'Well control',color='r')
        ax.scatter(xf,yf,marker='X',label = 'Fish',color = 'brown')
        ax.scatter(x,y,marker=9,label = 'Shoe',color="k")
        ax.plot(xc,yc,color='k')
        #plot.invert_xaxis()
        ax.invert_yaxis()
        ax.axes.xaxis.set_visible(False)
        leg = ax.legend(loc='best',frameon=False);
        #plt.show()
        plt.savefig(mypath1 + "STICK CHART.jpg")
        print(("------------------COMPLETED-----------------"))
        
        
        
        
        
        import sys
        from PIL import Image
        from win32com.client import Dispatch
        import pandas as pd
        import numpy as np
        import dataframe_image as dfi
        
        
        
        
        l = pd.read_excel("C:/Users/Jayaraj/Desktop/SOFTWARE TEST/RESULT/raw_OUTPUT(Losses).xlsx")
        t = pd.read_excel("C:/Users/Jayaraj/Desktop/SOFTWARE TEST/RESULT/raw_OUTPUT(TVD).xlsx")
        tg = pd.read_excel("C:/Users/Jayaraj/Desktop/SOFTWARE TEST/RESULT/raw_OUTPUT(TVD-graph).xlsx")
        w = pd.read_excel("C:/Users/Jayaraj/Desktop/SOFTWARE TEST/RESULT/raw_OUTPUT(wellcontrol).xlsx")
        f = pd.read_excel("C:/Users/Jayaraj/Desktop/SOFTWARE TEST/RESULT/raw_OUTPUT(fish).xlsx")
        
        
        
        dfl = l[['notes','depth_start','depth_end','time_from','time_to','duration','losses_raw']]
        dfw = w[['notes','depth_start','depth_end','time_from','time_to','duration','kick_raw']]
        dff = f[['notes','depth_start','depth_end','time_from','time_to','duration',]]
        dftg = tg[['csg_size','csd','c/l','v/d/h']]
        dftg1 = tg[['Casing size','CSD','C/L','V/D/H','X-axis','Y-axis']]
        
        
        
        

        dfil = dfl[['losses_raw','depth_start','depth_end']]
        dfil.set_index("losses_raw",inplace = True)
        dfil_styled = dfil #adding a gradient based on values in cell
        dfi.export(dfil_styled,mypath1+"loss.png")
        
        dfiw = dfw[['kick_raw','depth_start','depth_end']]
        dfiw.set_index("kick_raw",inplace = True)
        dfiw_styled = dfiw #adding a gradient based on values in cell
        dfi.export(dfiw_styled,mypath1+"kick.png")
        
        dfif = dff[['notes','depth_start','depth_end']]
        dfif.set_index('notes',inplace = True)
        dfif_styled = dfif #adding a gradient based on values in cell
        dfi.export(dfif_styled,mypath1+"fish.png")
        
        
        
        def get_concat_h_blank(im1, im2, color=(0, 0, 0)):
            dst = Image.new('RGB', (im1.width + im2.width, max(im1.height, im2.height)), color)
            dst.paste(im1, (0, 0))
            dst.paste(im2, (im1.width, 0))
            return dst
        
        def get_concat_v_blank(im1, im2, color=(0, 0, 0)):
            dst = Image.new('RGB', (max(im1.width, im2.width), im1.height + im2.height), color)
            dst.paste(im1, (0, 0))
            dst.paste(im2, (0, im1.height))
            return dst
        
        im1 = Image.open(mypath1 +'loss.png' )
        im2 = Image.open(mypath1 + 'kick.png')
        get_concat_h_blank(im1, im2, (255, 255, 255)).save(mypath1 + 'loss-kick.png') 
        
        
        im1 = Image.open(mypath1 +'loss-kick.png' )
        im2 = Image.open(mypath1 + 'fish.png')
        get_concat_h_blank(im1, im2, (255, 255, 255)).save(mypath1 + 'loss-kick-fish.png')
        
        im1 = Image.open(mypath1 +'STICK CHART.jpg' )
        im2 = Image.open(mypath1 + 'loss-kick-fish.png')
        get_concat_h_blank(im1, im2, (255, 255, 255)).save(mypath1 + 'final.png')
        
       
        
        
        get_concat_h_blank(im1, im2, (255, 255, 255)).save("C:/Users/Jayaraj/Desktop/SOFTWARE SHOWCASE/OUTPUT/STICK CHART.jpg") 
        
        
        
        
        
        a = "COMPLETED"
        st.header(a)
        a = "STICK CHART IS BELOW"
        st.text(a)
        
        img = load_image(mypath1 + 'final.png')
        st.image(img)
         
        img1 = load_image(mypath1 + 'Summary.png')
        st.image(img1)



main()






