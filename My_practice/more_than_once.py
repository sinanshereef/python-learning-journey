
# 8. Find Elements Appearing More Than Once
#
# Input: [1,2,3,2,4,1,2,5,3]
# Output: [1,2,3]

inp=[1,2,3,2,4,1,2,5,3]
lst=[]
dic={}
for i in inp:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for k,v in dic.items():
    if v>1:
        lst.append(k)
print(lst)