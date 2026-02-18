num=int(input("Enter the Number: "))
flag=0
for i in range(2,num,1):
    if num%i==0:
        flag=1
if flag>0:
    print("not a prime number")
else:
    print("Prime Number")