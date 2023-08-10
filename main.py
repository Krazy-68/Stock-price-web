import yfinance as yf
import streamlit as st
x = input("Shown are the stock **closing price** and ***volume*** of ")
name=x
st.write("""
# Simple Stock Price App
Shown are the stock **closing price** and ***volume*** of 
"""+name )
tickerSymbol = x
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)
