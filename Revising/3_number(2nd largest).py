num1=int(input("Enter the 1st Number:"))
num2=int(input("Enter the 2nd Number:"))
num3=int(input("Enter the 3rd Number:"))
if (num1>num2)&(num1>num3):
    if(num2>num3):
        print(num2,"is the 2nd largest")
    else:
        print(num3,"is the 2nd largest")
elif (num2>num1)&(num2>num3):
    if(num1>num3):
        print(num1,"is the 2nd largest")
    else:
        print(num3,"is the 2nd largest")
elif (num3>num1)&(num3>num2):
    if(num1>num2):
        print(num1,"is the 2nd largest")
    else:
        print(num2,"is the 2nd largest")
else:
    print("All are same Numbers")