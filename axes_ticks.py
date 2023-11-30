import matplotlib.pyplot as plt 

x = [10,20,30,40,10,20,50]
y = [10,40,20]

fig, ax = plt.subplots()
fig, ay = plt.subplots()

ax.plot(x)
ay.plot(y)

ax.set_xlabel('X-Axis')
ax.set_ylabel('Y-Axis')

ay.set_xlabel('X-Axis')
ay.set_ylabel('Y-Axis')
ay.set_xticks([0,1,2])

ax.grid(True, linestyle='--')
plt.show()
