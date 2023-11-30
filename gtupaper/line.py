import matplotlib
import matplotlib.pyplot as plt

a= [20,30,60,50]
b= [10,20,30,40]

plt.plot(a,label='a')
plt.plot(b,label='b')

plt.legend(loc=6)
plt.grid()
plt.show()

