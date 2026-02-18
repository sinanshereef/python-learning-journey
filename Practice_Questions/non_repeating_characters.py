from Practice_Questions.least_count import min_val

# Write a program to find the first non-repeating character in a string.
# Example: 'swiss' → Output: 'w'


str=input('Enter the Character: ')
dic={}
for i in str:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
min_val=min(dic,key=dic.get)
print(min_val)