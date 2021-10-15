from abc import ABC, abstractmethod
#abstract class has atleast one abstract method in the class...
#abstract method are methods that have declaration but no definition
#abstract class can be used to set restriction on 
#on the the class that will inherith so that methods on
#the abstract class must be defined on the the child class
# class Computer(ABC):
#     myattri = 'My name'
# #you cannot create an obj of abstract class.. .i.e. com = Computer()
# #to make an abstract class, we import ABC and abstractmethod 
# #method having declaration  but not definition
# #is called abstract method s
 
# #a class having an abstract method is 
# #called abstract class
#     @abstractmethod
#     def process(self):
#         pass

#     # @abstractmethod
#     # def process2(self):
#     #     pass


# class Laptop(Computer):
#     def process(self):
#         print('It is running')

 
# # com = Computer()
# com1 = Laptop()
# com1.process()
# # print(com1.myattri)

class Computer(ABC):
    myattri = 'My name'
#you cannot create an obj of abstract class.. .i.e. com = Computer()
#to make an abstract class, we import ABC and abstractmethod 
#method having declaration  but not definition
#is called abstract method s
 
#a class having an abstract method is 
#called abstract class
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print('It is running')


class WhiteBoard:
    def write(self):
        print('its  writing')




class Programmer:
    def work(self, com):
        print('Solving Bugs')
        com.process()

com1 =  Laptop()
com2 = WhiteBoard()
prog1 =  Programmer()
prog1.work(com2) 