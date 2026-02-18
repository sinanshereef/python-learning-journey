

lst=[i**2 for i in range(1,31) if i%2==0]
print(lst)

         #OR

lst=[(i,i**2) for i in range(1,31) if i%2==0]
print(lst)