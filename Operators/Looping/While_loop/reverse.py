num=int(input("Enter the Number:"))#153
rev=0
while(num!=0):
    digit=num%10
    rev=(rev*10)+digit
    num//=10
print(rev)

