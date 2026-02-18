
# 🧮 10. Find All Unique Combinations That Sum to Target
#
# Question:
# Input: [2,3,6,7], target=7
# Output: [ [7], [2,2,3] ]

lst1=[2,3,6,7]
target=7
count=0
for i in lst1:
    count+=i
    if target==count:
        print(count)