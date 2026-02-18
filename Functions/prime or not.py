

def prime():
    num=int(input("enter the number: "))
    flag=0
    for i in range(2,num,1):
        if num%i==0:
            flag=1
    if flag>0:
        print("The given number is not Prime")
    else:
        print("The Number is Prime")


prime()
