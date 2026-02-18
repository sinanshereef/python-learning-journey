

#Add square of Odd Numbers ranging 1-10.........

lst=[]
for i in range(1,11):
    if (i%2!=0):
        lst.append(i**2)
print(lst)