import pandas as pd

data = {'Age': [28, 24, 22, 30, 25]}

data2 = {'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'],
        'Age': [28, 24, 22, 30, 25],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Miami']}

df2 = pd.DataFrame(data2)
df = pd.DataFrame(data)
print(df.describe())
print(df2.tail(2))
print(df2.shape)