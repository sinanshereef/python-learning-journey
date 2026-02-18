


f=open("C:/Users/zinan/Downloads/sample4.txt",'r')
for i in f:
    data=i.rstrip("\n").split(',')
    loc=data[5]
    age=data[3]
    if loc=='chennai' and age>'23':
        print(data[1::2])


    # if data[5]=='Chennai':
    #     print(data[1:5])


    # if data[3]<'23':
    #     print(data[1:4])



    # if data[3]>'22':
    #     print(data[1:5])