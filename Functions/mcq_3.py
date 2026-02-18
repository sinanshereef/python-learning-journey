#implement Fibinocci series:...


def series():
    start=int(input("Enter the Number: "))
    second_number=int(input("Enter the Number: "))
    terms=int(input("How many terms?: "))
    if terms<=0:
        print(terms,"must be a positive number")
        return
    if terms==1:
        print(start)
        return

    print(start,end=" ")
    print(second_number,end=" ")

    for i in range(start,terms):
        c=start+second_number
        print(c,end=" ")
        start,second_number=second_number,c

series()

