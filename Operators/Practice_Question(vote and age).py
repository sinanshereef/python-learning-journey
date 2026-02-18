num=int(input("Enter your Age:"))
if num>=18:
    print("You can Vote")
elif num==17:
    print("You can learn to Drive")
elif num==16:
    print("They can Buy a Lottery Ticket")
elif num<16:
    print("You can go Tick or treating")
else:
    print("Invalid Symbol")