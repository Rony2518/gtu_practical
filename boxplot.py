import matplotlib.pyplot as plt
import numpy as np

# # Generate some example data
# np.random.seed(42)
# data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# # Create a box plot
# plt.boxplot(data, labels=['Dataset 1', 'Dataset 2', 'Dataset 3'])
# plt.title('Box Plot Example')
# plt.xlabel('Datasets')
# plt.ylabel('Values')

# # Show the plot
# plt.show()

x = [
    [1,2,4,6,8],
    [1,3,5,7,9],
]
#middle line is median
#upper line of box is third quatile
#lower line of box is  quatile
plt.boxplot(x)

plt.show()