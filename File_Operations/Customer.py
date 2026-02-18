

f=open("C:/Users/zinan/Downloads/customer1.txt",'r')
dic={}
for i in f:
    data=i.rstrip('\n').split(',')
    loc=data[-1]
    if loc not in dic:
        dic[loc]=1
    else:
        dic[loc]+=1

for k,v in dic.items():
    print(k,":",v)
    
#     prof=data[4]
#     if prof not in dic:
#         dic[prof]=1
#     else:
#         dic[prof]+=1
#
# for k,v in dic.items():
#     print(k,":",v)

    # loc=data[-1]
    # if prof=='Doctor' and loc=='india':
    #     print(data[1:4])

    # if prof=='Pilot':
    #     print(data[1:4])

    # loc=data[-1]
    # if prof=='Doctor' and loc=='uk':
    #     print(data[1:4])

    # if prof=='Doctor':
    #     print(data[1:4])

    # loc=data[5]
    # age=data[3]
    # if loc=='india' and age>'50':
    #     print(data[1:4])

    # if loc=='india':
    #     print(data[1:5])


    # if '25'<age<'40':
    #     print(data[1:6:2])

    # if age<'25':
    #     print(data[1:5])

    # if age>'50':
    #     print(data[1:5])