

# 🧠 LEVEL 4: Medium Logic Building
# Q10. Print Fibonacci Series up to N Terms
#
# Logic:
# Each number = sum of previous two numbers... eg: 1,2,3,5,8....

# num=int(input("Enter the Number: "))
# a=0
# b=1
# for i in range(num):
#     print(a,end=" ")
#     a,b=b,a+b


num=int(input("Enter the Number: "))
a=0
b=1
for i in range(num):
    print(a,end=' ')
    a,b=b,a+b