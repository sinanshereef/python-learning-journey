

f=open('num2','r')
even_lst=[]
odd_lst=[]
for i in f:
    num=int(i.rstrip('\n'))
    if(num%2==0):
        even_lst.append(num)
    else:
        odd_lst.append(num)
print(even_lst)
print(odd_lst)
print(sum(even_lst))
print(sum(odd_lst))
