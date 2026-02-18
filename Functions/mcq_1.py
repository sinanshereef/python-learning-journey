
def atm():
    for correct_pin in range(0,5):
        correct_pin=int(input("Enter the Pin: "))
        if correct_pin==1234:
            print("Please choose the service")
        break
        correct_pin+=1
    else:
        print("Card blocked after 5 incorrect attempts")


atm()


