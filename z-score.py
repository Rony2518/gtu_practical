from scipy import stats
import numpy as np

# Let's create a simple array
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Use scipy's zscore function
z_scores = stats.zscore(data)

print(z_scores)
