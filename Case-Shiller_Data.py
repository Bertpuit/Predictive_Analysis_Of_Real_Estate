import pandas_datareader as pdr
import datetime

# Define the ticker for the Case-Shiller Home Price Index from FRED
cs_ticker = "CSUSHPINSA"  # National Case-Shiller Home Price Index

# Define the time range
start = datetime.datetime(2000, 1, 1)  # Start date
end = datetime.datetime.now()  # End date as current date

# Fetch Case-Shiller Home Price Index data from FRED
cs_data = pdr.DataReader(cs_ticker, 'fred', start, end)

# The DataFrame 'cs_data' now holds the numerical data of the Case-Shiller Index
print(cs_data.head())  # Display the first few rows of the DataFrame
