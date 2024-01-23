import pandas_datareader as pdr
import matplotlib.pyplot as plt
import datetime

# Define the tickers for 2-year and 10-year Treasury bond yields from FRED
ticker_2y = "DGS2"  # FRED code for 2-year Treasury bond yield
ticker_10y = "DGS10"  # FRED code for 10-year Treasury bond yield
start = datetime.datetime(2020, 1, 1)
end = datetime.datetime(2021, 1, 1)

# Fetch data from FRED
data_2y = pdr.DataReader(ticker_2y, 'fred', start, end)
data_10y = pdr.DataReader(ticker_10y, 'fred', start, end)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(data_2y, label='2-Year Yield')
plt.plot(data_10y, label='10-Year Yield')
plt.title('2-Year vs 10-Year US Treasury Bond Yields')
plt.ylabel('Yield (%)')
plt.xlabel('Date')
plt.legend()
plt.grid(True)
plt.show()
