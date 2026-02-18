


#check the num and find the number is Amstrong or Not......


num=int(input("Enter the Number: ")) #153
temp=num
n=len(str(temp))
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**n
    temp//=10
if sum==num:
    print(f"{num} is an Amstrong")
else:
    print(f"{num} is not amstrong")


