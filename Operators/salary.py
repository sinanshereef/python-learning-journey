salary=int(input("Enter the salary of the user:"))
service=int(input("Enter the year of Service:"))
if service>=5:
    bonus = salary * 5 / 100
    print(bonus)
else:
    print("no bonus")