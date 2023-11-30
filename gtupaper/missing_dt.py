import pandas as pd
import numpy as np

dic = {
    "First Score": [10, 20, np.nan, 30],
    "Second Score": [25, 30, np.nan, 50],
    "Third Score": [10, 30, np.nan, 40],
}
df = pd.DataFrame(dic)
print(df)

#using fillna
mean_fill = df.fillna(df.mean())
mean_fill = mean_fill.round(1)
print(mean_fill)

#using dropna
drop_dt = df.dropna(axis=0).reset_index(drop=True)#reset index is optional, for del column we can use axis=1
print(drop_dt)

#using Interpolate
inter_ffill = df.interpolate(method="ffill")#newer version of python use df.ffill() function direct
inter_bfill = df.interpolate(method="bfill")#newer version of python use df.fbill() function direct
print(inter_ffill)#forward fill
print(inter_bfill)#backward fill
