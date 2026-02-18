from asyncio import ensure_future

#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *



for i in range(4):
    for j in range(4-i-1):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()

for i in range(2,-1,-1):
    for j in range(4-i-1):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()