
# 🧮 2. Find Words with Even Length in a Sentence
#
# Question:
# Input: "Python makes coding fun"
# Output: ['Python', 'makes', 'coding']

inp="Python makes coding fun"
lst=list(inp.split())
lst1=[]
for i in lst:
    if len(i)%2==0:
        lst1.append(i)
    else:
        pass
print(lst1)