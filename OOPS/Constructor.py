

class Car:
    vehicle_type='Car'
    def __init__(self,segment,model,fuel_type,cc):
        self.segment=segment
        self.model=model
        self.fuel_type=fuel_type
        self.cc=cc

    def fill_values(self):
        print(self.segment,self.model,self.fuel_type,self.cc,Car.vehicle_type)

car1=Car('suv','xuv500','Petrol',2000)
car1.fill_values()

car2=Car('sedan','Swift_dezire','CNG',1200)
car2.fill_values()

car3=Car('Jeep','Mahindra_Major','Diesal',1800)
car3.fill_values()