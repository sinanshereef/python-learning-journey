from os import remove

num=input("Enter the Numbers: ")
lst=[]
for i in num:
    lst.append(int(i))
def second_largest():
    lst.sort(reverse=True)
    largest=lst[0]
    while largest in lst:
        lst.remove(largest)
    second_larg=lst[0]
    print("The Second Largest Element is",second_larg)

second_largest()
