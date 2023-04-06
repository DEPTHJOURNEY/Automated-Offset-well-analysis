import pandas as pd
import streamlit as st

st.set_page_config(page_title='ONE-PLACE')
st.header("TEST")

st.write("df is taking")


# Read in data from the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)

def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=xlsx&gid=")
    return pd.read_excel(csv_url,sheet_name='Sheet2')
st.write("df is taking")
df = load_data(st.secrets["public_gsheets_url"])
st.write("df is taken")
st.dataframe(df)
# Print results.


for row in df.itertuples():
    #st.write(row)
    #st.write(df.columns)
    st.write(f"{row.name} is :{row.pet}:")
#st.write(df['code'])
