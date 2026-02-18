

class Person:
    def details(self,fname,lname,age,location):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.location=location


class Employee(Person):
    def identity(self,id,prof,dept,salary):
        self.id=id
        self.prof=prof
        self.dept=dept
        self.salary=salary

    def printvalues(self):
        print(self.id, self.fname, self.lname, self.age,self.prof,self.dept,self.salary,self.location)

person1=Employee()
person1.identity(100,'Big Data Engineer','Data Science','10cr')
person1.details('Sinan','Shereef',23,'Mannar')
person1.printvalues()
