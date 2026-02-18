
# adding 35 as 75.... solving this problem by converting tuple to list then list to tuple

tup=(10,15,20,25,30,35,40,45,100)
lst=list(tup)
lst[5]=75
tup=tuple(lst)
print(tup)