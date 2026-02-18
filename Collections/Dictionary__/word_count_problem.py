from os.path import split

#word Count......... O/P= car= number etc.........

sentence='car bike bat mouse bike car bus lorry bat bike car mouse bike rat cat car car cat bus'
word=sentence.split(' ')
dic={}
for i in word:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)