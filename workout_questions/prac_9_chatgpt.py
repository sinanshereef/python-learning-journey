

# Question 9: Print a Right-Angled Triangle Pattern
#
# Difficulty: Easy
# Problem: Write a program that prints a triangle pattern using * for n rows.
# Input: n = 4
# Output:
#
# *
# **
# ***
# ****


for i in range(4):
    for j in range(i+1):
        print("*",end="")
    print()