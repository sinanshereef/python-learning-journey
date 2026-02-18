

lst=[1,2,3,4,5,6,7,8,9]
f=list(filter(lambda num:num%2!=0,lst))
squares=list(map(lambda num:num**2,f))
print(squares)