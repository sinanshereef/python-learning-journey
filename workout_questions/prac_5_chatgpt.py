


# Question 5: Count Vowels in a String
#
# Difficulty: Easy-Medium
# Problem: Write a function that counts the number of vowels in a given string.
# Input: "hello world"
# Output: 3
# Hint: Check each character against "aeiouAEIOU".


def vowels():
    str=input("Enter the String: ")
    count=0
    ch='aeiouAEIOU'
    for i in str: #a
        if i in ch: #a=str
            count+=1
    print(count)

vowels()