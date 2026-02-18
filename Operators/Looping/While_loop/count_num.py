
#How many digits are there in the Number........

num=int(input("Enter the Number:"))
res=0
while(num!=0):
    num//=10
    res+=1
print(res)
