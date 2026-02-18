
 #create a list without duplicaes...........


lst1=[10,10,30,30,40,50,60,'ml','ml',300,"Big data"]
lst2=[]
for i in lst1:
    if i not in lst2:
        lst2.append(i)

print(lst2)
