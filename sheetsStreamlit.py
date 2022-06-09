# streamlit_app.py

import streamlit as st
from gsheetsdb import connect

# Create a connection object.
conn = connect()

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=10)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

tekst="Data=04062022"
sheet_url = st.secrets["public_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')
rowsData=run_query(f'SELECT * FROM "{sheet_url}" WHERE Data='04062022')
st.title('Test wizualizacji na wbe serwerze')
st.dataframe(rows)
st.line_chart(rows)
st.dataframe(rowsData)
#st.altair_chart(data['Konduktancja'])
# Print results.
#for row in rows:
#   st.dataframe(row)
