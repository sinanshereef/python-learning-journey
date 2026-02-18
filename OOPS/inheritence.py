
#Single Inheritence

class A: #Parent
    def printa(self,num1):
        self.num1=num1
        print('Inside class A',self.num1)

class B(A):#Child
    def printb(self,num2):
        self.num2=num2
        print('Inside Class B',self.num2)


obj1=B()
obj1.printa(100)
obj1.printb(200)