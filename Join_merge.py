import pandas as pd

data ={
    "Name": ["Ronak", "Ram", "Roshan"],
    "Enroll No": [39, 38, 37],
}
data2 ={
    "Name": ["Ronak", "Ram", "Roshan"],
    "Enroll No": [39, 38, 37],
    "English": [100, 60, 40],
}

df = pd.DataFrame(data)
df2 = pd.DataFrame(data2)
# concat = pd.concat([df,df2],axis=1)
Joined = df.join(df2.set_index(["Name","Enroll No"]),on=["Name","Enroll No"])
print(Joined)

merged = pd.merge(df,df2,on="Enroll No")