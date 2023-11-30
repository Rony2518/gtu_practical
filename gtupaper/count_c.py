import numpy as np

array = np.array([
    ['A','B','C','D'],
    ['B','C','C','A'],
    ['A','B','C','F']
])

count_c = np.sum(array=='C')
print(count_c)