import matplotlib.pyplot as plt
values1 = [1,2,3,4]
values2 = [1,4,9,16]
plt.plot(values1,label='line1',marker='.')
plt.plot(values2,label='line2',marker='v')
plt.xlabel("Xaxis")
plt.ylabel("Yaxis")
plt.title("Hello first Graph")
plt.legend()
plt.show()

