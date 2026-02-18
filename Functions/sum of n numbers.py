

# method 1

# def sum():
#     num=int(input("Enter the Number: "))
#     sum1=0
#     for i in range(1,num+1,1):
#         sum1+=i
#     print(sum1)
#
# sum()


#Method 2

# def sum(num):
#     sum1=0
#     for i in range(1,num+1):
#         sum1+=i
#     print(sum1)
#
# sum(5)


#Method 3

def sum(num):
    sum1=0
    for i in range(1,num+1):
        sum1+=i
    return sum1
data=sum(5)
print(data)

