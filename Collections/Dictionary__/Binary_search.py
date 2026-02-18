
lst=[10,50,30,2,500,342,399,122,1,5,8,101]
num=int(input("Enter the Number to be Searched: "))
lst.sort()
flag=0
low=0
upper=len(lst)-1
while(low<=upper):
    mid=(low+upper)//2  #5
    if num>lst[mid]:
        low=mid+1
    elif num<lst[mid]:
        upper=mid-1
    elif num==lst[mid]:
        flag=1
        break
if flag>0:
    print("Element Found")
else:
    print("Not Found")