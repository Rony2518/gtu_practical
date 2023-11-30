import numpy as np

X = int(input("Enter Number of Roows:"))
Y = int(input("Enter Number of columns:"))

arr = np.empty((X,Y))
r1 = np.random.rand(3,3)
for i in r1:
    for j in i:
        print(f"{j:.2f}",end=" ")
    print()

for i in range(X):
    for j in range(Y):
        arr[i][j]=(i+1)*(j+1)

print(arr)
print(arr[2,0])


