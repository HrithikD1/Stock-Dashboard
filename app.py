import pandas as pd
import streamlit as st
from datetime import date
import plotly.express as plt

DATE_COLUMN = 'Close'

today = date.today()

DATA_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRbOL-WcqCeq4dPNluZZ0SJk3aR7h0WV69sR7tLH5h6QU4TPWgqpMQ_ikKnUvOezsykoiiKn1ya-6dg/pub?output=csv"

def load_data(DATA_URL):
    data = pd.read_csv(DATA_URL)

    def lowercase(x): return str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

stock_data = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vRbOL-WcqCeq4dPNluZZ0SJk3aR7h0WV69sR7tLH5h6QU4TPWgqpMQ_ikKnUvOezsykoiiKn1ya-6dg/pub?output=csv")

data = load_data(DATA_URL)

st.header("Stock Dashboard")

st.subheader("Tata Steel Share Price (NSE:TATASTEEL)")

if st.checkbox('Show raw data for the stock above'):
    st.subheader('Raw data')
    st.write(data)

st._arrow_bar_chart(data)


stock2 = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vTYPBJFDhpUt73QjL3zi4CABWDbdBYUjA-e7Q8IB61pDHAh4bo32GC3TKFUl_q2AIaSUQtP4bae2zkO/pub?output=csv")

data1 = load_data("https://docs.google.com/spreadsheets/d/e/2PACX-1vTYPBJFDhpUt73QjL3zi4CABWDbdBYUjA-e7Q8IB61pDHAh4bo32GC3TKFUl_q2AIaSUQtP4bae2zkO/pub?output=csv")

st.subheader("Reliance Power (NSE:RPOWER)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data1)

st._arrow_bar_chart(data1)

