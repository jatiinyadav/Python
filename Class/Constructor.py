class A:

    def __init__(self):
        print("In A __init__")

    def feature1(self):
        print("Feature 1-A is working")
    def feature2(self):
        print("Feature 1-B is working")


class B:

    def __init__(self):
        super().__init__()
        print("In B __init__")
    
    def feature1(self):
        print("Feature 2-A is working")
    def feature2(self):
        print("Feature 2-B is working")

class C(A,B):

    def __init__(self):
        super().__init__()
        print("In C __init__")

    def feature1(self):
        super().feature1()

a1 = C() 

a1.feature1()                           #Here Class A will be called due to Method Resolution Order it goes from left to right
# b1 = B()
