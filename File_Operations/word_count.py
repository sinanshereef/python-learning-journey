

f=open('words','r')
dic={}
for i in f:
    word1=i.strip().split(' ')
    for j in word1:
        if j not in dic:
            dic[j]=1
        else:
            dic[j]+=1
for k,v in dic.items():
    print(k,':',v)