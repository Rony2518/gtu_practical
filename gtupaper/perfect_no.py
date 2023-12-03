n = int(input("Enter a number:"))
sum = 0
mul = 1
while(n>0):
    rem = n % 10
    sum = sum + rem
    mul = mul * rem
    n = n // 10
if(sum==mul):
    print("Perfect Number")
else:
    print("Not a Perfect Number")