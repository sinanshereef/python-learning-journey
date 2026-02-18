lower=int(input("Enter the Lower Limit:"))
upper=int(input("Enter the Upper Limit:"))
while(lower<=upper):
    if lower % 5==0:
        print(lower)
    lower+=1