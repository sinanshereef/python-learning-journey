


# def fact():
#     num1=int(input("Enter the 1st Number: "))
#     res=1
#     for i in range(1,num1+1,1):
#         res+=i
#     print(res)
#
# fact()

# def fact(num1,res):
#     num1=int(input("Enter the 1st Number: "))
#     res=1
#     for i in range(1,num1+1,1):
#         res+=i
#     print(res)
#
# fact()



def fact(num1):
    res=1
    for i in range(1,num1+1,1):
        res*=i
    return res
data=fact(4)
print(data)
