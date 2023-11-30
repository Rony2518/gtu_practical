import pandas as pd

Data = {
    'Name': ['A','A', 'B', 'C'],
    'Age': [20, 20, 30, 40],
}

df = pd.DataFrame(Data).drop_duplicates().reset_index()
print(df)

import numpy as np

a = np.array([10,20,30,40,50,20,10,50])

print(a)
print(np.unique(a))