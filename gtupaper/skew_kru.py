import numpy as np
from scipy.stats import skew, kurtosis

# Sample dataset
data = np.array([2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7, 7, 8])

# Calculate skewness and kurtosis
skewness_value = skew(data)
kurtosis_value = kurtosis(data)

# Display the results
print("Dataset:", data)
print("Skewness:", skewness_value)
print("Kurtosis:", kurtosis_value)
