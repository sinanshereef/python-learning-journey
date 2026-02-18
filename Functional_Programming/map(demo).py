

# To Find the Square of the List[1,2,3,4,5,6,7,8,9]

lst=[1,2,3,4,5,6,7,8,9]

def squares(num):
    return num**2

lst1=list(map(squares,lst))
print(lst1)

   #OR

lst1=list(map(lambda num:num**2,lst))
print(lst1)