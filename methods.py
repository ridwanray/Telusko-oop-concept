#instance methods
#class methods
#static methods

class Student:
    school = "Telusko"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return (self.m1 + self.m2 + self.m3)

    # def get_m1(self): #getter ...accessor
    #     return self.m1

    # def set_m1(self, value): #setter mutator
    #     self.m1 = value
    @classmethod
    def getSchool(cls):
        return cls.school
    @staticmethod
    def info():
        print('This is student class... in abc')

    
s1 = Student(34,45,45)
s2 = Student(23,34,34)

print(s1.avg())
# print(s1.get_m1())

print(Student.getSchool())

Student.info()
#if you want to create a var which has nothing
#to do with the class var, and nothing to do with the instance var
#like we want to do sth diffeen

