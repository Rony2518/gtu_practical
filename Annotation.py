import matplotlib.pyplot as plt

plt.plot([1,3,4,5,6],[1,5,3,4,2], marker='o', label="Line 1")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.annotate("Seond Point",xy=(3,5))
plt.legend()
plt.show()