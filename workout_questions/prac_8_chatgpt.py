

# Question 8: Palindrome Checker
#
# Difficulty: Easy-Medium
# Problem: Write a program to check if a given string is a palindrome.
# Input: "madam"
# Output: True
# Hint: A palindrome reads the same backward and forward.

str=input("Enter the String: ")
reverse=str[::-1]
if str==reverse:
    print(True)
else:
    print(False)
    