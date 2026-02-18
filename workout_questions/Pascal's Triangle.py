


# Pascal's Triangle Starts from 1... and There's a Magic Formula to find next number in a Row by using Previous One's....
# The Formula is: num*(i-j)//(j+1)
# Output Should be:
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1



def Pascals_triangle(n):
    for i in range(n):
        num=1
        for j in range(n-i-1):
            print("",end=" ")
        for j in range(i+1):
            print(num,end=' ')
            num=num*(i-j)//(j+1)
        print()

Pascals_triangle(5)