list1=['drt','skp','dimp','drs','simp','drd','5']
list2=[]

#same object Count 1st and Last...

for i in list1:
    if len(i)>1:
        if (i[0]==i[-1]):
            list2.append(i)
print(list2)