

# 🧠 8. Find Common Elements Between Two Lists
#
# Example:
# Input: [1,2,3,4], [3,4,5,6]
# Output: [3,4]


lst1=[1,2,3,4]
lst2=[3,4,5,6]
lst3=[]
for i in lst1:
    if i in lst2:
        lst3.append(i)
print(lst3)