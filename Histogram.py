import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
data = np.random.randn(1000)  # 1000 random data points

# Create a histogram
plt.hist(data, bins=5, edgecolor='black')  # Adjust the number of bins as needed

# Add labels and title
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Simple Histogram Example')

# Display the histogram
plt.show()
