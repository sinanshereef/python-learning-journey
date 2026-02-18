

# Question 6: List of Squares
#
# Difficulty: Easy
# Problem: Write a program to generate a list containing squares of numbers from 1 to n.
# Input: n = 5
# Output: [1, 4, 9, 16, 25]
# Hint: Use a list comprehension.


n=int(input("Enter the Number: "))
lst=[]
for i in range(1,n+1):  #1-5
    lst.append(i**2)
print(lst)