# overloading 
# we are calling the same method name but the
# arguments are different or types of the args.

 
# i.e.  + (Plus).. we are calling  __add__() but diffrent arguments

# i.e 
# Student :#method overloading.. 2 method with the same name with
#          #different parameters... concept  Not present in python
#     def average(a,b):

#     def average(a,b,c):

class Student:
     def __init__(self, m1,m2):
        self.m1=m1
        self.m2 = m2
        
     def sum(self,a=None,b=None,c=None):

          s = 0
          if a!=None and b!= None and c!=None:
               s = a+b+c
          elif a!=None and b!= None:
               s= a+b
          else:
               s = a
          return s

s1 =  Student(58,69)

print(s1.sum(5))
print(s1.sum(5,6))
print(s1.sum(5,6,10))

 

 ##Method overloading  