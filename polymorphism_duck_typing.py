#Poly Morphism....i.e many forms
#loose coupling
#dependency injection
#interface 

#Four way of implementing in python
#Duck Typing 
#operator Overloading
#Method Overloading
#Method overriding

# x = 5
# x = 'Navin'
class Pycharm:
    def execute(self):
        print('compiling')
        print('Running ')

class MyEditor:
    def execute(self):
        print('Spell Check')
        print('Convention Check')
        print('complinig')
        print('running')

     

class Laptop:
    def code(self, ide):
        ide.execute()

# ide = Pycharm()  
ide = MyEditor()  
lap1 = Laptop()
lap1.code(ide)