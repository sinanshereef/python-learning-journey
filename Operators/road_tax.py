price=int(input("Enter the Price of the Bike:"))
if price>100000:
    per=(price*15)/100
    print("percentage=",per)
elif 50000 <= price <= 100000:
    per2 = (price * 10) / 100
    print("percentage=",per2)
else:
    per3 = (price * 5) / 100
    print("percentage=",per3)
