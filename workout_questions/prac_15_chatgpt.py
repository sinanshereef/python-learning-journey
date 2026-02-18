

# Question 16: Fibonacci Sequence
#
# Difficulty: Easy-Medium
# Problem: Write a program to print the first n Fibonacci numbers.
# Input: n = 6
# Output: 0 1 1 2 3 5

num=int(input("Enter the Number: "))
a=0
b=1
lst=[]
for i in range(num):
    lst.append(a)
    temp=a+b
    a=b
    b=temp
print(lst)