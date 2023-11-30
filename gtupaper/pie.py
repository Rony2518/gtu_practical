import matplotlib.pyplot as plt

v = [5,8,9,20,4]

plt.pie(v,explode=(0,0,0,0.2,0),labels=['A','B','C','D','E'],shadow=True,autopct='%1.0f%%')
plt.show()