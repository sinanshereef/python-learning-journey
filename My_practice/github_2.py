
# Q. Write a program which can compute the factorial of a given numbers.

def fact():
    fac=1
    num=int(input('Enter the Number: '))
    for i in range(1,num+1):
        fac=fac*i
    print(fac)

fact()
