from OOPS.oops_demo import person1


class Person:
    def setvalues(self,f_name,l_name,age,gender,location):
        self.f_name=f_name
        self.l_name=l_name
        self.age=age
        self.gender=gender
        self.location=location

    def printvalues(self):
        print(self.f_name,self.l_name,self.age,self.gender,self.location)

person1=Person()
person1.setvalues('Sinan','Shereef',23,'Male','Mannar')
person1.printvalues()

person2=Person()
person2.setvalues('Deepak','Prasad',20,'male','Kollam')
person2.printvalues()

person3=Person()
person3.setvalues('Jithu','B.Philip',21,'Male','Pathanamthitta')
person3.printvalues()

person4=Person()
person4.setvalues('Vinay','Madhu',21,'Male','Kannur')
person4.printvalues()
