import pandas_datareader as pdr
import matplotlib.pyplot as plt
import datetime

# Define the ticker for the Case-Shiller Home Price Index from FRED
# Here, we'll use the national index as an example. You can replace it with a specific metro area code if needed.
cs_ticker = "CSUSHPINSA"  # National Case-Shiller Home Price Index

# Define the time range
start = datetime.datetime(2000, 1, 1)  # You can adjust the start date
end = datetime.datetime.now()  # Current date as end date

# Fetch Case-Shiller Home Price Index data from FRED
cs_data = pdr.DataReader(cs_ticker, 'fred', start, end)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(cs_data, label='Case-Shiller Home Price Index')
plt.title('Case-Shiller Home Price Index Over Time')
plt.ylabel('Index Value')
plt.xlabel('Year')
plt.legend()
plt.grid(True)
plt.show()
