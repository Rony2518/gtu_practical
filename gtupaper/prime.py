n = int(input("Enter a Number:"))

def prime(n):
    flag=0
    for i in range(2,n):
        if(n%i==0):
            flag=1
            break
    if(flag==1):
        print(n,"is not a prime")
    else:
        print(n,"is a prime")
prime(n)