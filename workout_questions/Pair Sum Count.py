

# Pair Sum Count

total=int(input("Enter the Number: ")) #6
arr1=input("Enter the Numbers: ")
print(arr1)
arr=[(i,j) for i in arr1 for j in arr1 if int(i)+int(j)==total]
print(arr)
