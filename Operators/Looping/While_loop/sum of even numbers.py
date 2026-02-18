lower=int(input("Enter the Lower limit:"))
upper=int(input("Enter the upper Limit:"))
sum=0
while(lower<=upper):
    if lower%2==0:
        sum=sum+lower
    lower+=1
print(sum)