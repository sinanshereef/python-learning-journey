

f=open("C:/Users/zinan/Downloads/customer1.txt",'r')
f1=open('customer_details','w')
dic={}
for i in f:
    data=i.strip().split(',')
    prof=data[4]
    if prof not in dic:
        dic[prof]=1
    else:
        dic[prof]+=1
for k,v in dic.items():
    res=k+':'+str(v)+'\n'
    f1.write(res)
