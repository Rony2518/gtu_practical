n = int(input("Enter n:"))
t=n  
r=0
sum=0
while(t>0):
    r = t%10
    sum += r**3
    t = t//10
if(sum==n):
    print("Armstrong number")
else:
    print("Not")
