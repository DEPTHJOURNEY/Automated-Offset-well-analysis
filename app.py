
import pdfplumber
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import re
from datetime import datetime
import plotly.graph_objects as go

st.set_page_config(page_title='ONE-PLACE')

url = "https://github.com/JVJayarah3/Automated-Offset-well-analysis/blob/main/IADC_WELL_RPT.xlsx?raw=true"

#print(df)


#path = "F:/iadc-deep shah/IADC-LAST WELL/"

#print("restarting///////......")
#df1 = pd.read_excel(path+"IADC_WELL_RPT.xlsx")

df1 = pd.read_excel(url)

st.header("ONE-REPORT")
#st.header("PROCESSING")
df1['rig_no'] = df1['rig_no'].replace('-',"Select")
select_rig = df1['rig_no'].unique()
add_select_box_rig_no = st.sidebar.selectbox("RIG-NO",(select_rig))
submit_rig_no = st.sidebar.button("SUBMIT-RIG NO")
#df1_selected_rig = df1[df1['rig_no'] ==add_select_box_rig_no ]


select_well = df1['well_no'].unique()
add_select_box_well_no= st.sidebar.selectbox("WELL-NO",(select_well))
submit_well_no = st.sidebar.button("SUBMIT-WELL NO")


select_month = df1['month_wise'].unique()
add_select_box_month_no= st.sidebar.selectbox("SELECT-MONTH",(select_month))
submit_month = st.sidebar.button("SUBMIT-MONTH")

select_color = df1["color"].unique()
add_select_box_color= st.sidebar.selectbox("HIGHLIGHTED-PROBLEMS",(select_color))
submit_color = st.sidebar.button("SUBMIT-PROBLEMS")

df1['Time_count'] = df1['Time_count'].replace('-',"")
df1['Time_count'] = df1['Time_count'].replace('',np.nan,regex=True)
df1['Time_count'] = df1['Time_count'].astype(float)


#buttons = []
#for r in df2['date']:
#    buttons.append(st.button(str(r)))
def color(s):
    if s.color == 'RED':
        return ['background-color: lightcoral']*len(s) 
    if s.color == 'BLUE': 
         ['background-color: cornflowerblue']*len(s) 
    if s.color=='YELLOW':
        return ['background-color: gold']*len(s) 
    #if s.COLOR=='WHITE':
     #   ['background-color: mediumseagreen']*len(s)
   # if s.COLOR=='BLACK':
    #    ['background-color: silver']*len(s)

  

    
if submit_rig_no:
   
    #st.dataframe(df1[df1['rig_no']==add_select_box_rig_no])
    df_rig_no = df1[df1['rig_no']==add_select_box_rig_no]
    
    #rblist = pd.DataFrame()
    #rblist['date'] = df_rig_no[df_rig_no['color']=='RED']['date'].unique()
    
    hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """

# Inject CSS with Markdown
    st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)
    
    
    
    st.dataframe(df_rig_no[['date','IADC_DESC','Time_count','activity','color','well_no']])
    
    df_graph=df_rig_no.dropna(subset=['Time_count'])
    elapsedtime = pd.DataFrame()
    elapsedtime['IADC_DESC'] = df_rig_no['IADC_DESC']
    elapsedtime['Time_count'] = df_rig_no['Time_count']
    elapsedtime = elapsedtime.groupby(by=elapsedtime['IADC_DESC']).sum()
    #ax.pie(elapsedtime['ELAPSED_TIME'],labels = elapsedtime.index)
    #ax.legend(title='OPERATIONAL TIME DISTRIBUTION')
    fig_rig = go.Figure(
        go.Pie(
        labels = elapsedtime.index,
        values =elapsedtime['Time_count'],
        hoverinfo = "label+percent",
        textinfo = "value"
    ))
    st.plotly_chart(fig_rig)

    #print(elapsedtime)
    #elapsedtime.to_excel(path+"testttt.xlsx")
    #plt.show()
    
    
    
    
    
if submit_well_no:
    #st.dataframe(df1[(df1['well_no']==add_select_box_well_no) & (df1['rig_no']==add_select_box_rig_no)])   
    df_rig_no = df1[(df1['well_no']==add_select_box_well_no) & (df1['rig_no']==add_select_box_rig_no)]
    
    hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """

# Inject CSS with Markdown
    st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)
    
    
    
    
    st.dataframe(df_rig_no[['date','IADC_DESC','Time_count','activity','color','well_no']])
    df_graph=df_rig_no.dropna(subset=['Time_count'])
    elapsedtime = pd.DataFrame()
    elapsedtime['IADC_DESC'] = df_rig_no['IADC_DESC']
    elapsedtime['Time_count'] = df_rig_no['Time_count']
    elapsedtime = elapsedtime.groupby(by=elapsedtime['IADC_DESC']).sum()
    #elapsedtime = df_graph.groupby(by=df_graph['code']).sum()
    #ax.pie(elapsedtime['ELAPSED_TIME'],labels = elapsedtime.index)
    #ax.legend(title='OPERATIONAL TIME DISTRIBUTION')
    fig_rig = go.Figure(
        go.Pie(
        labels = elapsedtime.index,
        values =elapsedtime['Time_count'],
        hoverinfo = "label+percent",
        textinfo = "value"
    ))
    st.plotly_chart(fig_rig)





if submit_month:
    #st.dataframe(df1[(df1['month_wise']==add_select_box_month_no) & (df1['rig_no']==add_select_box_rig_no)])   
    if add_select_box_well_no == "-":    
        df_rig_no = df1[(df1['month_wise']==add_select_box_month_no) & (df1['rig_no']==add_select_box_rig_no)]
    else:
        df_rig_no = df1[(df1['month_wise']==add_select_box_month_no) & (df1['rig_no']==add_select_box_rig_no) &(df1['well_no']==add_select_box_well_no)]
   
    hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """

# Inject CSS with Markdown
    st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)
    
    
    st.dataframe(df_rig_no[['date','IADC_DESC','Time_count','activity','color','well_no']])
    df_graph=df_rig_no.dropna(subset=['Time_count'])
    elapsedtime = pd.DataFrame()
    elapsedtime['IADC_DESC'] = df_rig_no['IADC_DESC']
    elapsedtime['Time_count'] = df_rig_no['Time_count']
    elapsedtime = elapsedtime.groupby(by=elapsedtime['IADC_DESC']).sum()
    #elapsedtime = df_graph.groupby(by=df_graph['code']).sum()
    #ax.pie(elapsedtime['ELAPSED_TIME'],labels = elapsedtime.index)
    #ax.legend(title='OPERATIONAL TIME DISTRIBUTION')
    fig_rig = go.Figure(
        go.Pie(
        labels = elapsedtime.index,
        values =elapsedtime['Time_count'],
        hoverinfo = "label+percent",
        textinfo = "value"
    ))
    st.plotly_chart(fig_rig)



if submit_color:
    hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """

# Inject CSS with Markdown
    st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)
    if add_select_box_well_no == "-" and add_select_box_month_no =="-":    
        df_rig_no = df1[(df1['color']==add_select_box_color) & (df1['rig_no']==add_select_box_rig_no)]
    elif add_select_box_well_no != "-" and add_select_box_month_no =="-":
        df_rig_no = df1[(df1['color']==add_select_box_color) & (df1['rig_no']==add_select_box_rig_no) & (df1['well_no'] ==add_select_box_well_no) ]
    elif add_select_box_well_no == "-" and add_select_box_month_no !="-":
        df_rig_no = df1[(df1['color']==add_select_box_color) & (df1['rig_no']==add_select_box_rig_no) & (df1['month_wise']==add_select_box_month_no)]
    elif add_select_box_well_no != "-" and add_select_box_month_no !="-":
        df_rig_no = df1[(df1['color']==add_select_box_color) & (df1['rig_no']==add_select_box_rig_no) & (df1['well_no'] ==add_select_box_well_no) & (df1['month_wise']==add_select_box_month_no)]
        
   
    st.dataframe(df_rig_no[['date','IADC_DESC','Time_count','activity','color','well_no']])
    elapsedtime = pd.DataFrame()
    elapsedtime['IADC_DESC'] = df_rig_no['IADC_DESC']
    elapsedtime['Time_count'] = df_rig_no['Time_count']
    elapsedtime = elapsedtime.groupby(by=elapsedtime['IADC_DESC']).sum()
    #elapsedtime = df_graph.groupby(by=df_graph['code']).sum()
    #ax.pie(elapsedtime['ELAPSED_TIME'],labels = elapsedtime.index)
    #ax.legend(title='OPERATIONAL TIME DISTRIBUTION')
    fig_rig = go.Figure(
        go.Pie(
        labels = elapsedtime.index,
        values =elapsedtime['Time_count'],
        hoverinfo = "label+percent",
        textinfo = "value"
    ))
    st.plotly_chart(fig_rig)
