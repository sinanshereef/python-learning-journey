



# Difficulty: Medium
# Problem: Write a program to count the frequency of each character in a string.
# Input: "banana"
# Output: {'b': 1, 'a': 3, 'n': 2}

str=input("Enter the String: ")
letter=list(str)
dic={}
for i in letter:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)