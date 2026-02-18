#check the given year is leap year or not?....


def year():
    num=int(input("Enter the Year: "))
    if num % 4==0 and num % 100!=0 or num % 400==0:
        print(num,"is a Leap year")
    else:
        print(num,"is not a leap year")

year()
