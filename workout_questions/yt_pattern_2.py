


# Output.....
#
#       *
#     *   *
#    *  *  *



# row=int(input("Enter the Range: "))
# for i in range(0,row):
#     for j in range(0,row-i-1):
#         print(end=" ")
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()


def pyramid():
    n = int(input("Enter the Range: "))
    for i in range(n):
        for j in range(0,n-i-1):
            print(" ",end=" ")
        for j in range(0,i+1):
            print(" * ",end=" ")
        print()

pyramid()
