class  A:

    def __init__(self):
        print('in A init')


    def feature1(self):
        print('feature 1 A working')
    
    def feature2(self):
        print('feature 2 working')



#if there is no init in B, it is going to go up.. i.e in A
# class  B(A):
    
#     def __init__(self):
#         # super().__init__()
#         print('in B init')


#     def feature3(self):
#         print('feature 3 working')
    
#     def feature4(self):
#         print('feature 4 working')


class  B():
    
    def __init__(self):
        # super().__init__()
        print('in B init')


    def feature1(self):
        print('feature 1 b working')
    
    def feature4(self):
        print('feature 4 working')

class C(A,B):
    def __init__(self):
        super().__init__()
        print('in C init')

    def feat(self):
        super().feature1()


#by default when there is multiple inheritance,
#is starts from Left to Right
a1 = C()
a1.feat()
# a1.feature1()
# a1 = B()




