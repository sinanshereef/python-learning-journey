

# Question 11: Remove Duplicates from a List
#
# Difficulty: Medium
# Problem: Write a program to remove duplicates from a list while preserving order.
# Input: [1, 2, 2, 3, 4, 4, 5]
# Output: [1, 2, 3, 4, 5]

lst1=[1, 2, 2, 3, 4, 4, 5]
lst2=[]
for i in lst1:
    if i not in lst2:
        lst2.append(i)
print(lst2)