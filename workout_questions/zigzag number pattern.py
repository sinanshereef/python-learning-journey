# Logic...( Give Spaces when even reached) rowil tanne...
# The Output Should be:
# 1 2 3
#   4 5 6
# 7 8 9


def zigzag(n):
    num=1
    for i in range(1,n+1): #1,2,3
        if (i%2==0):
            print(" ",end=" ")
        for j in range(1,n+1):
            print(num,end=" ")
            num+=1
        print()

zigzag(3)
