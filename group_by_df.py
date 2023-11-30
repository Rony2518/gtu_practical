import pandas as pd

# import os
# print(os.getcwd())

# df = pd.read_csv("D:/python/gtupaper/nba.csv")
# # print(df)
# teamgroup = df.groupby("Team")
# for Name, Team in teamgroup:
#     print(Name)
#     print(Team)

# data = {
#     "Team": [
#         "Riders",
#         "Riders",
#         "Devils",
#         "Devils",
#         "Kings",
#         "kings",
#         "Kings",
#         "Kings",
#         "Riders",
#         "Royals",
#         "Royals",
#         "Riders",
#     ],
#     "Rank": [1, 2, 2, 3, 3, 4, 1, 1, 2, 4, 1, 2],
#     "Year": [2014, 2015, 2014, 2015, 2014, 2015, 2016, 2017, 2016, 2014, 2015, 2017],
#     "Points": [876, 789, 863, 673, 741, 812, 756, 788, 694, 701, 884, 690],
# }

# df2 = pd.DataFrame(data)
# print(df2)
# teamgroup = df2.groupby("Team")
# for Name, Team in teamgroup:
#     print(Name)
#     print(Team)

data = {
    'Name':['A','B','A','B','A','B', 'A','B'],
    'Score':[10,20,20,30,40,10,40,10]
}

df = pd.DataFrame(data).groupby('Name').sum()#we can apply mean() or anything it's like separate array
print(df)