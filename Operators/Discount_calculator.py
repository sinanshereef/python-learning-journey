price=int(input("Enter the Orginal Price:"))
discount_perc=int(input("Enter the Discount Percentage:"))
discount=price*(discount_perc/100)
finalprice=price-discount
print(discount)
print(finalprice)