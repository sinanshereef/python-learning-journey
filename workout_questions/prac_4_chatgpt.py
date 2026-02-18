
# Question 4: Multiplication Table
#
# Difficulty: Easy
# Problem: Write a program to print the multiplication table of a given number up to 10.
# Input: 3
# Output:
# 3 x 1 = 3
# 3 x 2 = 6
# ...
# 3 x 10 = 30


def mul():
    num=int(input("Enter the Number: ")) #3
    for i in range(1,11):   #1
        res=num*i   #3*1=3
        print(num,"*",i,"=",res)

mul()