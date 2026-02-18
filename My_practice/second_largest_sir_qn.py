
# Second largest number
# Find the second largest element in a list without sorting


lst=[2,4,6,8,19,33,75,45,20,54,68,52,98,98]
lst1=set(lst)
lst2=list(lst1)
lst2.sort(reverse=True)
second_largest=lst2[1]
print(second_largest)