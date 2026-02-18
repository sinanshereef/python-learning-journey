


class Employee:
    dept='Artificial Intelligence'
    company='Deloitte'
    def details(self,id,fname,lname,age,prof,salary):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
        self.prof=prof
        self.salary=salary

    def values(self):
        print(self.id,self.fname,self.lname,self.age,self.prof,Employee.dept,Employee.company,self.salary)

emp1=Employee()
emp1.details(100,'Sinan','Shereef',23,'AI Engineer','10Cr')
emp1.values()

emp2=Employee()
emp2.details(101,'Deepak','Prasad',20,'Data Scientist','10Cr')
emp2.values()

emp3=Employee()
emp3.details(102,'Vinay','Kannur',20,'Big data Engineer','10Cr')
emp3.values()

emp4=Employee()
emp4.details(104,'Jithu','B.Philip',21,'Data Scientist','10Cr')
emp4.values()

emp5=Employee()
emp5.details(105,'Steeve','Sunny',20,'AI Engineer','10Cr')
emp5.values()