

# 🧩 3. Remove Duplicates Without Using Set
#
# Question:
# Remove duplicates from a list while maintaining order.
#
# Example:
# Input: [1,2,2,3,1,4,2]
# Output: [1,2,3,4]

lst=[1,2,2,3,1,4,2]
new_lst=[]
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
    else:
        continue
print(new_lst)