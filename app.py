import pandas
import streamlit as st

stock_data = pandas.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vRbOL-WcqCeq4dPNluZZ0SJk3aR7h0WV69sR7tLH5h6QU4TPWgqpMQ_ikKnUvOezsykoiiKn1ya-6dg/pub?output=csv")

print(stock_data)
