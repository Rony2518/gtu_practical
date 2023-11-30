import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# Sample time series data
data = {
    'Date': ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01'],
    'Value': [100, 120, 110, 130, 150]
}

# Convert 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Create a DataFrame
df = pd.DataFrame(data)

# Plot the time series data
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Value'], marker='o', linestyle='-')
plt.title('Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.show()
