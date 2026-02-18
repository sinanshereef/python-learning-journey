

# Write a program to find the character that appears the least number of times (excluding spaces).
# Example: 'mississippi' → 'm' appears once.

character=input('Enter the Character: ')
dic={}
for i in character:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1

min_val=min(dic,key=dic.get)
print(min_val,'appears',dic[min_val])