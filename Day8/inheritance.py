#Example1:
# class A:
#     def m1(self):
#         print("This is metho of class A")
# class B(A):
#     def m2(self):
#         print("This is method of class B")
# res=B()
# res.m1()
# res.m2()

#Example:    Single Inheritance
# class A:
#     a, b=100, 200
#     def m1(self):
#         print(self.a+self.b)
# class B(A):
#     x,y=30,20
#     def m2(self):
#         print(self.x-self.y)
#
# res=B()
# res.m1()    #300
# res.m2()    #10

#Example: multilevel inheritance
# class A:
#     a,b=100,200
#     def m1(self):
#         print(self.a+self.b)
# class B(A):
#     x ,y=50,26
#     def m2(self):
#         print(self.x-self.y)
# class C(B):
#     p,r=1000,3000
#     def m3(self):
#         print(self.p*self.r)
#
# res=C()
# res.m1()    #300
# res.m2()    #24
# res.m3()    #3000000

#Example Heirarchy inheritance

# class A:
#     a,b=100,200
#     def m1(self):
#         print(self.a+self.b)
# class B(A):
#     x,y=40,30
#     def m2(self):
#         print(self.x+self.y)
# class C(A):
#     p,r=3000,5000
#     def m3(self):
#         print(self.p/self.r)
#
# res1=B()
# res2=C()
# res1.m2()   #70
# res2.m3()   #0.6
# res2.m1()   #300
# res1.m1()   #300

#Example5
# class A:
#     a,b=100,200
#     def m1(self):
#         print(self.a+self.b)
# class B:
#     x,y=50,60
#     def m2(self):
#         print(self.x,self.y)
# class C(A,B):
#     p,q = 10001,20001
#     def m3(self):
#         print(self.p,self.q)
#
# res=C()     #300
# res.m1()    #50 60
# res.m2()
# res.m3()    #10001 20001

#Example6:      calling parent class method using child class(super())
# class A:
#     def m1(self):
#         print("This is method of class A")
# class B(A):
#     def m1(self):
#         print("This is method of class B")
#         super().m1()
# res=B()
#
# res.m1()    #This is method of class B
#             #This is method of class A

#Example7:
# class A:
#     a,b=10,20
# class B(A):
#     i,j=80,70
#     def m1(self):
#         x,y=30,40
#         print(x+y)
#         print(self.i+self.j)
#         print(self.a+self.b)
# res=B()
# res.m1()

#Example8: overridding varibales
# class A:
#     name = "John"
# class B(A):
#     name = "Scott"
#
# res=B()
# print(res.name)     #Scott

#Example9: overridding methods
# class Bank:
#     def rateOfIntrest(self):
#         return 0
# class XBank(Bank):
#     def rateOfIntrest(self):
#         return 10
# class YBank(Bank):
#     def rateOfIntrest(self):
#         return 20
#
# obj=Bank()
# print(obj.rateOfIntrest())      #0
#
#
# objX=XBank()
# print(objX.rateOfIntrest())     #10
#
# objY=YBank()
# print(objY.rateOfIntrest())     #20

#Example10: overloading(polymorphisam)
# class Human:
#     def myfun(self,name=None):
#         if name is not None:
#             print("Hello " + name)
#         else:
#             print("Hello")
# h=Human()
# h.myfun("Scott")
# h.myfun()

#Example11: overloading 2
class calculation:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)
res=calculation()
res.add()           #0
res.add(10,20)      #30
res.add(10,20,30)   #60

















