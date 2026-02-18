

f=open('C:/Users/zinan/PycharmProjects/JulyDSbatch/Identifiers/sample3','r')
lst=[]
for i in f:
    stripped=i.strip()
    if stripped:
        lst.append(int(stripped))
print(lst)
print(sum(lst))

#     lst.append(int(i.rstrip("\n")))
# print(lst)
# print(sum(lst))
