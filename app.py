import datetime
import streamlit as st 
import yfinance as yf


st.write("""
            # Stock Price Analyser""")


#get data for Apple's stock
# symbol = "AAPL"

symbol = st.selectbox(
    'Which Stock symbol would you want to analyze?',
    ('APPL', 'GOOG', 'TSLA','MSFT','NFLX'))

#to show in one line both start and end date col
col1,col2 = st.columns(2)

with col1:
    start_date = st.date_input("Please enter start date", datetime.date(2019, 7, 6))

with col2:
    end_date = st.date_input("Please enter end date", datetime.date(2019, 7, 10))


#in this coming different lines
# start_date = st.date_input("Please enter start date", datetime.date(2019, 7, 6))  #by default this date if not used anything
# end_date = st.date_input("Please enter end date", datetime.date(2019, 7, 10))


ticker_data = yf.Ticker(symbol)
ticker_df = ticker_data.history(period="1d",start=start_date,end=end_date)   # here we need daily data for 4 years
 
st.write(f"""
            ### {symbol}'s Stock Price Data""")


#dataframe is a tabular structure with rows and cols
st.dataframe(ticker_df)

st.write(f"""
            ### {symbol}'s Closing Price Chart Data""")
#( f""" statement """ -> f string is to format the string with the selected symbol )

st.line_chart(ticker_df["Close"])

st.write(f"""
            ### {symbol}'s Volume Chart""")

st.line_chart(ticker_df["Volume"])