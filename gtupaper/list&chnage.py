# f = int(input("Enter first Position:"))
# s = int(input("Enter Second Position:"))

# L1 = [1,2,3,4,5,6,7,8,9]
# print("Original List: ",L1)
# if 1<=f<=len(L1) and 1<=s<=len(L1):
#     t=L1[f-1]
#     L1[f-1]=L1[s-1]
#     L1[s-1]=t
#     print("List After Swapping: ",L1)
# else:
#     print("Invailid Position it should in beetween of 1 to ",len(L1))
f= int(input("Enter first pos:"))
s= int(input("Enter second pos:"))

L1 = [1,2,3,4,6,7]
print(L1)
if 0<=f<=len(L1) and 0<=s<=len(L1):
    t=L1[f]
    L1[f]=L1[s]
    L1[s]=t
    print(L1)
else:
    print("Invalid position")