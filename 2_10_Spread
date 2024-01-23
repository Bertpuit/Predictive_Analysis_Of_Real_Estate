import pandas_datareader as pdr
import matplotlib.pyplot as plt
import datetime

# Define the tickers for 2-year and 10-year Treasury bond yields from FRED
ticker_2y = "DGS2"  # FRED code for 2-year Treasury bond yield
ticker_10y = "DGS10"  # FRED code for 10-year Treasury bond yield
start = datetime.datetime(2020, 1, 1)
end = datetime.datetime(2024, 1, 1)

# Fetch data from FRED
data_2y = pdr.DataReader(ticker_2y, 'fred', start, end)
data_10y = pdr.DataReader(ticker_10y, 'fred', start, end)

# Aligning both datasets on the same dates
combined_data = pd.concat([data_2y, data_10y], axis=1)
combined_data.columns = ['2Y', '10Y']

# Drop rows where either column (2Y or 10Y) is NaN
combined_data.dropna(inplace=True)

# Calculate the yield spread (10-year yield minus 2-year yield)
combined_data['Spread'] = combined_data['10Y'] - combined_data['2Y']

# Plotting the yield spread
plt.figure(figsize=(10, 6))
plt.plot(combined_data['Spread'], label='10-Year minus 2-Year Yield Spread')
plt.title('Yield Curve Spread (10Y - 2Y)')
plt.ylabel('Yield Spread (Percentage Points)')
plt.xlabel('Date')
plt.legend()
plt.grid(True)
plt.show()
