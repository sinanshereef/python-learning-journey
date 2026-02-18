lower=int(input("Enter the Lower: "))
upper=int(input("Enter the upper: "))
even_sum=0
odd_sum=0
for i in range(lower,upper+1,1):
    if i % 2==0:
        even_sum+=i
    else:
        odd_sum+=i
print(even_sum)
print(odd_sum)