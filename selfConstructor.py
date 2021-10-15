class Computer:
    def __init__(self):
        self.name = "Navin"
        self.age =  20

    def update(self):
        self.age = 20
    
    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return

c1 = Computer()
c2 = Computer()

if c1.compare(c2):
    print('they are the same')
