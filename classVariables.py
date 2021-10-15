class Car:
    #class variables is defined in here, i.e outside init 
    #class name space
    #class var also called static var
    wheels = 4
    def __init__(self):
        self.mil = 10     # instance variables is defined in init
        self.com = 'BMW'   # Instance name space

c1 = Car()
c2 = Car()


c1.newVar = 'New Var'
Car.wheels = 23 # updating the wheel class
Car.anotherwheels = 90 #setting a new class instance
print(c1.com, c1.mil, c1.wheels, c1.anotherwheels, c1.newVar )
print(c2.com, c2.mil, c2.wheels, c1.anotherwheels)