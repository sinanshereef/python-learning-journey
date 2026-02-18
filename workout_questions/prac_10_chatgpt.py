

# Question 10: Sum of Digits
#
# Difficulty: Easy-Medium
# Problem: Write a program to calculate the sum of digits of an integer.
# Input: 1234
# Output: 10


def numb(num):
    total_sum=0
    while num!=0:
        digit=num%10  #1234%10
        total_sum+=digit
        num//=10
    print(total_sum)

numb(1234)