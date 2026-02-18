
dic={'car':2500,'bus':7000,'bike':500,'cycle':100,'jeep':3000,'Truck':4000}
lst=[i.upper() for i in dic if dic[i]>3000]
print(lst)