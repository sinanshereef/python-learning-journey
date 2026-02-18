

#   *
#  * *
# * * *
#  * *
#   *

def pyramid():
    n=3
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end=" ")
        for j in range(i+1):
            print(" * ",end=" ")
        print()

    for i in range(n-1,0,-1): #2,0
        for j in range(n-i): #3-2=1
            print(" ",end=" ")
        for j in range(i):
            print(" * ",end=" ")
        print()

pyramid()
