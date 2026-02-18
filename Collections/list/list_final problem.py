

# check the user given number is found or not on the list (Linear Search Algorithm).....

# Drawback= Time Complexity

lst=[1,2,3,4565,67,78,8,34,23,230,2323]
num=int(input("Enter the Number: "))
flag=0
for i in lst:
    if i==num:
        flag=1
        break
if flag>0:
    print("Found")
else:
    print("Not Found")

            # OR

for i in lst:
    if i==num:
        print("Found")
        break
else:
    print("Not Found")