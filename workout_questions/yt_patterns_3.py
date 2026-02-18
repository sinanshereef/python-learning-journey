

# Output..........
#
# * * * *
#  * * *
#   * *
#    *



num=int(input("Enter the Range: "))
for i in range(num,0,-1): #rows
    for j in range(0,num-i): #spaces
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()