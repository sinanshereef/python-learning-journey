unit=int(input("Enter the Unit:"))
if unit<=100:
    bill=unit*0
    print(bill)
elif 101 >= unit >= 200:
    bill=unit-100*5
    print(bill)
else:
    price=(unit-200)*10+500
    print(price)