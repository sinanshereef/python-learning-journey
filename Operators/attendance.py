class_held=int(input("Enter the Number of classes held:"))
attended=int(input("Enter the Number of classes attended:"))
perc=attended/class_held*100
if perc>=75:
    print("The allowed to sit in the exam hall and your attendance percentage =",perc)
else:
    print("you are not allowed to sit in the exam and ur attendance percentage =",perc)
