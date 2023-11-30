n = int(input("enter a number:"))
f=1
for i in range(1,n+1):
    f*=i
print(f)

def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
print(factorial(n))

def factorial(n):
    if(n==1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(n))