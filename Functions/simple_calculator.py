


def add(num1,num2):
    sum=num1+num2
    return sum

def sub(num1,num2):
    diff=num1-num2
    return diff

def mul(num1,num2):
    pro=num1*num2
    return pro

def div(num1,num2):
    res=num1/num2
    return res

print("1. Addition \n"
      "2. Subtraction \n"
      "3. Multiplication \n"
      "4. Division ")

num_1=int(input("Enter the 1st Number: "))
num_2=int(input("Enter the 2nd Number: "))
choice=int(input("Enter the Choice:"))

if(choice==1):
    print(num_1,"+",num_2,"=",add(num_1,num_2))
elif(choice==2):
    print(num_1,"-",num_2,"=",sub(num_1,num_2))
elif(choice==3):
    print(num_1,"*",num_2,"=",mul(num_1,num_2))
elif(choice==4):
    print(num_1,"/",num_2,"=",div(num_1,num_2))
else:
    print("Invalid")