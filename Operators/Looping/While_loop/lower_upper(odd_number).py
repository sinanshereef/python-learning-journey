lower=int(input("Enter the Lower limit:"))
upper=int(input("Enter the Upper limit:"))
sum=0
while(lower<=upper):
    if lower%2==1:
        sum+=lower
    lower+=1
print(sum)
