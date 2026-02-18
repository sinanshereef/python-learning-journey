lower=int(input("Enter the Lower Limit:"))
upper=int(input("Enter the Upper Limit:"))
sum1=0
sum2=0
while(lower<=upper):
    if lower % 2==0:
        sum1+=lower
    else:
        sum2+=lower
    lower+=1
print("Even Number:",sum1)
print("odd number:",sum2)