
# 🧮 9. Flatten a Nested List
#
# Question:
# Input: [[1,2], [3,4,5], [6]] → Output: [1,2,3,4,5,6]

inp=[[1,2],[3,4,5],[6]]
lst=[]
for i in inp:
    for j in i:
        lst.append(j)
print(lst)