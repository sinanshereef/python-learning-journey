


string='Luminar Technolab is a IT Finishing school at Kakkand'
data=string.split(' ')
list1=[]
for i in data:
    if len(i)>4:
        list1.append(i)

print(list1)