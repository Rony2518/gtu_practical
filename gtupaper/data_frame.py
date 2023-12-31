import pandas as pd
import numpy as np

data = {
    "Name": ["Ronak", "Ram", "Roshan"],
    "Enroll No": [39, 38, 37],
    "English": [100, 60, 40],
    "Maths": [100, 60, 40],
    "Science": [100, 60, 40],
}
dataframe = pd.DataFrame(data, index=[0,1,2])

first = dataframe[dataframe["Name"] == "Ronak"]

print(
    data,
    "\n\n",
    dataframe,
    "\n\n",
    first,
    "\n\n",
    dataframe[["Name", "English", "Maths", "Science"]],
    "\n\n",
    dataframe.loc[0],
    "\n\n",
    dataframe.loc[0, 'Enroll No']
)

dataframe['Per(%)']=(dataframe['English']+dataframe['Maths']+dataframe['Science'])/3

print(dataframe)
