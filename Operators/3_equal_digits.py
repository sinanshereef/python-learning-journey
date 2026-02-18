num=int(input("Enter a 3 digit Number:"))
hundreds= num//100
tens= num//100 % 10
units=num % 10
if hundreds==tens and tens==units:
    print("All the digits are Equals")
else:
    print("All the 3 digit numbers are not equals")