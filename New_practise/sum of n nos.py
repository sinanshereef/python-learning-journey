

# Sum of First N Numbers
#
# Logic:
# Use a loop or formula → sum = n*(n+1)//2.

num=int(input("Enter the Number: "))
sum=0
for i in range(num+1):
    sum+=i
print(sum)