import matplotlib
import matplotlib.pyplot as plt

data = [20,30,40,50,90]

plt.pie(data,labels=['A','B','C','D','E'],explode=(0,0,0,0,0.2),shadow=True,autopct='%1.0f%%')
plt.legend(loc=9)
plt.show()