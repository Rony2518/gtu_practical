# (1)
rows = 4
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
print("\n")
# (2)
rows = 4
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print("$", end=" ")
    print()
print("\n")
n = 5
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print("$",end=" ")
    print("\n")
# (3)
n=5
for i in range(n):
    for j in range(n):
        if i <= n // 2:  
            if j >= i and j < n - i:
                print("#", end=" ")
            else:
                print(" ", end=" ")
        else:  
            if j >= n - 1 - i and j <= i:
                print("#", end=" ")
            else:
                print(" ", end=" ")
    print()




