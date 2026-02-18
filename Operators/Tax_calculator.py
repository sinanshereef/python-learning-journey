income=int(input("Enter the Annual income:"))
if income<=250000:
    print("No tax")
elif 250001<=income<=500000:
    total=(income*5)/100
    print(total,"is the total")
elif 500001<=income<=1000000:
    total=(income*20)/100
    print(Total,"is the total")
else:
    total=(income*30)/100
    print(total,"is the total")