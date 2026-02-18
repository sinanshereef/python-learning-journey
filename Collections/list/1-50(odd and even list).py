

# 1. add elements into an empty set ranging 1-50
# 2. add even elements into an empty set ranging 1-50
# 3. add odd elements into an empty set ranging 1-50


list1=[]
sum1=0
for i in range(1,51):
    list1.append(i)
    sum1+=i
print(list1)

list2=[]
sum2=0
for i in range(1,51):
    if (i%2==0):
        list2.append(i)
        sum2+=i
print(list2)

list3=[]
sum3=0
for i in range(1,51):
    if(i%2!=0):
        list3.append(i)
        sum3+=i
print(list3)

print(sum1)
print(sum2)
print(sum3)
