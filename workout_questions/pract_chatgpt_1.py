
#   CHATGPT QUESTIONS.....

# Question 1: Sum of Natural Numbers
#
# Difficulty: Easy
# Problem: Write a program to calculate the sum of the first n natural numbers using a loop.
# Input: n = 5
# Output: 15

def numbers(num):
    sum=0
    for i in range(0,num+1):
        sum+=i
    print(sum)

numbers(5)