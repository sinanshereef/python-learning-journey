

# 1) Palindromic number pyramid (pattern)
#
# Task: Print a palindromic number pyramid for n rows. Example for n=4:
#
#       1
#     1 2 1
#   1 2 3 2 1
# 1 2 3 4 3 2 1

for i in range(4):
    for j in range(4-i-1):
        print(" ",end=" ")
    for j in range(i+2):
        print(j,end=' ')
    # for j in range(i,0,-1):
    #     print(j,end=' ')
    print()
