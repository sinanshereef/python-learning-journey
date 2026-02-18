

# 4. Write a program to check whether a string has duplicate characters or not.
# Example: 'unique' → Output: Yes (since 'u' appears more than once)


char=input('Enter the Character: ')
dic={}
flag=0
for i in char:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1

min_val=min(dic,key=dic.get)
max_val=max(dic,key=dic.get)
if dic[max_val]>1:
    print('yes',max_val,'appears more than once')
else:
    print('No Duplicates')