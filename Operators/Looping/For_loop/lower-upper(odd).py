
lower=int(input("Enter the Lower: "))
upper=int(input("Enter the upper: "))
for i in range(lower,upper+1,1):
    if i % 2!=0:
        print(i)