

#Union Operation......

lst1={1,2,3,4,5,6,7}
lst2={2,3,5,7,8,90,4}
lst=lst1.union(lst2)
print(lst)

#Intersection Operation...

lst1={1,2,3,4,5,6,7}
lst2={2,3,5,7,8,90,4}
lst=lst1.intersection(lst2)
print(lst)

#Difference Operation........(Item present in A, not in B)

lst1={1,2,3,4,5,6,7}
lst2={2,3,5,7,8,90,4}
lst=lst1.difference(lst2) #or lst1-lst2
print(lst)