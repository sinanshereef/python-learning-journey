

# Sum of Evens

num=int(input("Enter the Number: "))
sum=0
for i in range(0,num+1):
    if i%2==0:
        sum+=i
    else:
        pass
print(sum)
