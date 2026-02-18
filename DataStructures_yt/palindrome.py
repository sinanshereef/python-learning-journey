
n=121
num=n
result=0
while num!=0:
    id=num%10
    result=(result*10)+id
    num//=10
if result==n:
    print('Palindrome')
else:
    print('Not a Palindrome')