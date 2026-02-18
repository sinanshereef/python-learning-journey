

# Nested List.........

# A nested list is created inside a list so a nested list is act as a value...........

lst=[[100,'Rohan',20,"Tester",1200],[101,'Tom',23,"Analyst",1300],[103,'sabu',32,'Big data',1400],[104,'Mathai',35,'Senior_Developer',1500]]
total_salary=0
for i in lst:
    total_salary+=i[-1]
    print(i)
print(total_salary)
