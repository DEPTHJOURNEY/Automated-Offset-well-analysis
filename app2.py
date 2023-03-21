import pandas as pd
import streamlit as st

st.set_page_config(page_title='ONE-PLACE')
st.header("TEST")

st.write("df is taking")


# Read in data from the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)

def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)
st.write("df is taking")
df = load_data(st.secrets["public_gsheets_url"])

# Print results.
st.write("df is taken")
for row in df.itertuples():
    st.write(f"{row.name} is :{row.pet}:")
#st.write(df['code'])
