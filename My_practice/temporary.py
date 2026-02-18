

str='hello world'
new=str.split()
print(len(new[-1]))

nums=[1,1,2,3,2,4]
lst=[]
for i in nums:
        if i not in lst:
                lst.append(i)
print(lst)