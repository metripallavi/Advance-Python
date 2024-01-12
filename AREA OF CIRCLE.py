class function:
    pi=3.142
    r=0
    a=0

    def __init__(self,pi,r):
        self.pi=pi
        self.r=r

    def calculate(self):
        self.a=self.pi*self.r*self.r

    def input(self):
        self.r=input("enter radius")

    def funprints(self):
        print("r=",self.r,"a=",self.a)


x=function(0,0)
x.input()
x.calculate()
x.funprints()