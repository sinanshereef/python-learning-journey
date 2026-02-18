lst=[100,34,53,445,22,414,4,3,322,44]
lst.sort()
num=int(input("Enter the Number that to be searched: "))
low=0
upper=len(lst)-1  #9
mid=(low+upper)//2   #(0+9)//2=4
if num>lst[mid]:
    low=mid+1
    for i in range(low,upper+1):
        if num in lst:
            print("Found")
            break
        else:
            print("Not Found")
            break
elif num<lst[mid]:
    upper=mid-1
    for i in range(low, upper + 1):
        if num in lst:
            print("Found")
            break
        else:
            print("Not Found")
            break
elif num==lst[mid]:
    for i in range(low, upper + 1):
        if num in lst:
            print("Found")
            break
        else:
            print("Not Found")
            break
else:
    print("Not Found")