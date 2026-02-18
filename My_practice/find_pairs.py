

# 🧠 1. Find All Pairs with Given Sum
#
# Question:
# Given a list of numbers and a target, print all pairs that sum up to the target.
#
# Example:
# Input: [2, 4, 3, 5, 7, 8, 9], target = 10
# Output: (2,8), (3,7), (4,6)

lst=[2,4,3,5,7,8,9]
new_lst=[2,4,3,5,7,8,9]
target=10
for i in lst:
    for j in new_lst:
        if int(i+j==target):
            print((i,j))
        else:
            continue
