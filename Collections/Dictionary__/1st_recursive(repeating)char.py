
# First Recursive


patterns='ABCGSBAREBSASER'
dic={}
for i in patterns:
    if i not in dic:
        dic[i]=1
    else:
        print(i)
        break