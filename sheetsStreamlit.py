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

sheet_url = st.secrets["public_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')


st.title('Test wizualizacji na wbe serwerze')
st.dataframe(rows)
print(rows)
st.line_chart(rows)
#st.line_chart(data['Konduktancja'])
#st.altair_chart(data['Konduktancja'])
#st.line_chart(dat['Temperatura'])
# Print results.
#for row in rows:
#   st.dataframe(row)
