

class Student:
    coll_name='IIET'
    def details(self,id,fname,lname,age,course):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
        self.course=course

    def values(self):
        print(self.id,self.fname,self.lname,self.age,self.course,Student.coll_name)

student1=Student()
student1.details(101,'Rohit','Jaybharati',22,'Full Stack')
student1.values()

student2=Student()
student2.details(102,'Asif','Jayabharati',22,'Software')
student2.values()

student3=Student()
student3.details(103,'Afthab','Calicut',23,'Bussiness')
student3.values()

student4=Student()
student4.details(104,'Bharath','Mannar',23,'BCA')
student4.values()