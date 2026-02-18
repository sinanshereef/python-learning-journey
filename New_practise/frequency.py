
# Find Frequency of Each Character in a String
#
# Logic:
# Use dictionary to count.

charact=input("Enter the character: ")
dic={}
for i in charact:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1

for k,v in dic.items():
    print(k,":",v)