import pandas as pd
import streamlit as st

st.write("APP WORKING!")

tickers = ['AAPL','MSFT','NFLX','IBM','DIS','AXP','BA','CAT','CSCO','CVX','DWDP','GE','GS']
ticker = st.selectbox("Pick a ticker", tickers) 

df = pd.read_csv(ticker+".csv", parse_dates=['Date'], index_col=['Date'])

begDATE = df.index.min()
endDATE = df.index.max()

pickStart = st.sidebar.date_input("Pick start date:",begDATE, min_value=begDATE)
pickEnd = st.sidebar.date_input("Pick end date:",endDATE)
st.write(df.loc[pickStart:pickEnd])

st.write(begDATE)
st.write(endDATE)
