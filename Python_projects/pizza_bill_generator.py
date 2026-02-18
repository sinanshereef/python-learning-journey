
#------Pizza_Bill_Generator_____

#Based on a user's order, work out their final bill.
#Small Pizza: Rs.15
#Medium Pizza: Rs.20  #20+2
#Large Pizza: Rs.25
#Pepperoni for Small Pizza: +Rs.2
#Pepperoni for Medium or Large Pizza: +Rs.3
#Extra cheese for any size pizza: + Rs.1

print('___Welcome to Your Favorite Pizza Delivery Spot___')
size_pizza=input("Which pizza size would you like—S, M, or L?: ").upper()
add_pepperoni=input("Should I add pepperoni? Y/N: ").upper()
extra_cheese=input("Would you like extra cheese? Y/N: ").upper()

bill=0
price=0
pepperoni=0
cheese_charge=0

if size_pizza=='S':
    bill+=15
    price=15
    size_name='Small'
elif size_pizza=='M':
    bill+=20
    price=20
    size_name = 'Medium'
elif size_pizza == 'L':
    bill += 25
    price=25
    size_name = 'Large'
else:
    print("Invalid pizza size!")

if add_pepperoni=='Y':
    if size_pizza=='S':
        bill+=2
        pepperoni=2
    else:
        bill+=3
        pepperoni=3
if extra_cheese=='Y':
    bill+=1
    cheese_charge=1
print(f"""------------------------------------------
        PIZZA ORDER SUMMARY
------------------------------------------
Pizza Size       : {size_name}
Pepperoni        : {add_pepperoni}
Extra Cheese     : {extra_cheese}
------------------------------------------
Base Price       : {price}
Pepperoni Charge : {pepperoni}
Cheese Charge    : {cheese_charge}
------------------------------------------
YOUR FINAL BILL  : {bill}
------------------------------------------

Thank you for ordering! Enjoy your meal!""")