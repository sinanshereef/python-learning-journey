mark1=int(input("Enter the mark of 1st subject:"))
mark2=int(input("Enter the mark of 2nd subject:"))
mark3=int(input("Enter the mark of 3rd subject:"))
mark4=int(input("Enter the mark of 4th subject:"))
total_mark=mark1+mark2+mark3+mark4
print(total_mark)
if total_mark>=180:
    print("A+")
elif 160 <= total_mark <= 179:
    print("A")
elif 140 <= total_mark <= 159:
    print("B+")
elif 120 <= total_mark <= 139:
    print("B")
elif 100 <= total_mark <= 119:
    print("C+")
elif 80 <= total_mark <= 99:
    print("C")
else:
    print("FAIL")