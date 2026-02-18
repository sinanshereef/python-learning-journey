

# 🔢 2. Count Frequency of Each Element
#
# Question:
# Count how many times each element appears in a list.
#
# Example:
# Input: [1, 2, 2, 3, 1, 4, 2]
# Output: {1:2, 2:3, 3:1, 4:1}

lst=[1,2,2,3,1,4,2]
dic={}
for i in lst:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1

print(dic)