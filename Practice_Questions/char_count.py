

# Write a program to count and display the frequency of each character in the string.
# Example: 'apple' → {'a':1, 'p':2, 'l':1, 'e':1}


char=input('Enter the String: ')
dic={}
for i in char:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1

print(dic)