num1=int(input("Enter the year:"))
if num1 % 4==0 and num1 % 100!=0 or num1 % 400==0:
    print("True")
else:
    print("False")
