

# Write a program to count character frequencies without considering case (i.e., 'A' and 'a' are the same).
# Example: 'AppleEapple' → 'a':2, 'p':4, 'l':2, 'e':2

str='AppleEapple'
str1=str.lower()
dic={}
for i in str1:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)