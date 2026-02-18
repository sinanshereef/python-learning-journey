

list1=[10,1,3,5,4,2,6,8,7,20]
num=int(input("Enter the Number: "))
for i in list1:
    for j in list1:
        if (i+j==num):
            print(i,j)
            