

# Add 1-25 Range elements which is Divisible by 5 into the list.........

list1=[]
for i in range(1,26):
    if (i%5==0):
        list1.append(i)
print(list1)