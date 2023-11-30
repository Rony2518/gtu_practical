#######Using pandas#########
import pandas as pd

Data = {
    'Name': ['A','A', 'B', 'C'],
    'Age': [20, 20, 30, 40],
}

df = pd.DataFrame(Data).drop_duplicates().reset_index(drop=True)#reset_index(drop=True) is optional 
# df2 = df.drop_duplicates() #we can also do it in separate lines
print(df)
#######Using numpy#########
import numpy as np

a = np.array([10,20,30,40,50,20,10,50])

print(a)
print(np.unique(a))