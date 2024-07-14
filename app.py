import pandas as pd
import streamlit as st

# URL of the Google Sheets CSV data
DATA_URL = "https://docs.google.com/spreadsheets/d/1keb0D3P9V0xNJXHKBvvuIwmXBQO2AU1c5uV82W-WDyM/gviz/tq?tqx=out:csv&sheet=Sheet1"

def load_data(url):
    data = pd.read_csv(url)
    data.columns = data.columns.str.lower()  # Convert all column names to lowercase
    return data

# Load data from Google Sheets
tata_steel_data = load_data(DATA_URL)

# Streamlit app
st.header("Stock Dashboard")

# Tata Steel
st.subheader("Tata Steel Share Price")

if st.checkbox('Show raw data for Tata Steel'):
    st.subheader('Raw data')
    st.write(tata_steel_data)

# Ensure the 'date' column is in datetime format
tata_steel_data['date'] = pd.to_datetime(tata_steel_data['date'])

# Display line chart for Tata Steel
st.subheader("Closing Price Line Graph")
st.line_chart(tata_steel_data.set_index('date')['close'])

# Display bar chart for Tata Steel
st.subheader("Closing Price Bar Chart")
st.bar_chart(tata_steel_data.set_index('date')['close'])

# Display first and last closing prices
first_value = tata_steel_data['close'].iloc[0]
last_value = tata_steel_data['close'].iloc[-1]

st.subheader("First and Last Closing Prices")
st.write({
    "First Closing Price": first_value,
    "Last Closing Price": last_value
})
