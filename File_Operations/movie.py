


f=open("C:/Users/zinan/Downloads/movies.csv",'r')
dic={}
for i in f:
    data=i.rstrip('\n').split(',')
    rate=data[3]
    year=data[2]
    if year>'2005' and rate>'4':
        print(data[1:4])

    # if rate>'4':
    #     print(data[1:4])

#     year=data[2]
#     if year not in dic:
#         dic[year]=1
#     else:
#         dic[year]+=1
# for k,v in dic.items():
#     print(k,':',v)


    # if '1975'<=year<='2000':
    #     print(data[1:4])

    # if year>'2000':
    #     print(data[1:4])