class Computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print(f"My configuration {self.ram}  {self.cpu}")



com1  = Computer('i5', 16)
com2  = Computer('i3', 20)

com1.config()
com2.config()

