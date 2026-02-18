
# 1.Write a program to find the character that appears the most number of times in a string.
#   Example: 'banana' → 'a' appears 3 times.


character=input("Enter the Character: ")
dic={}
count=0
for i in character:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
max_val=max(dic,key=dic.get)
print(max_val,"appears",dic[max_val])
# for k,v in dic.items():
#     print(k,':',v)

