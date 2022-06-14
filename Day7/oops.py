#Example1:
# class MyClass:
#     def fun(self):
#         pass
#     def display(self,name):
#         print(name)
#
# mc1=MyClass()
# mc1.fun()
# mc1.display("scott")

#Example2:
# class infosys:
#     def project(self,name):
#         print(name)
#     def training(self,date):
#         print(date)
# infy=infosys()
# infy.project("citibank")
# infy.training("06/17/2021")

#Example:
# class myclass:
#     def m1(self):
#         print("this is instance method")
#     @staticmethod
#     def m2(self,num):
#         print(self,num)
# res=myclass()
# res.m1()                #this is instance method
# myclass.m2(200,300)     #200 300  calling static method directly using class

#Example: Class variable
# class myclass:
#     a,b =10,20
#     def add(self):
#         print(self.a+self.b)
#     def mul(self):
#         print(self.a*self.b)
#
# res=myclass()
# res.add()       #30
# res.mul()       #200

#Example:

# i,j=10,20       #global variables
# class myclass:
#     a,b=20,30   #class variables
#     def add(self,x,y):     #local variables
#
#         print(x+y)  #90
#         print(i-j)  #-10
#         print(x*y)  #2000
#
# res=myclass()
# res.add(40,50)

#Example5:
# a,b=10,20       #global variables
# class myclass:
#     a,b=20,30   #class variables
#     def add(self,a,b):     #local variables
#
#         print(a+b)  #300    local variable
#         print(self.a-self.b)  #-10  class variable
#         print(globals()['a']+globals()['b'])  #30   global variable
#
# res=myclass()
# res.add(100,200)

#Example6: one class can have multiple objects
# class myclass:
#     def display(self,name):
#         print('This is display method')
#         print(name)
#
# obj1=myclass()
# obj1.display("John")
#
# obj2=myclass()
# obj2.display("Scott")
#
# obj3=myclass()
# obj3.display("David")

# #Example7: constructor example
# class myclass:
#     def __init__(self):
#         print('this is constructor')
#     def m1(self):
#         print('this is method')
#
# res=myclass()   #invoke constructor automatically
# res.m1()        #method we call explicitely by using method

#Example8: parameterised constructor
# class myclass:
#     name = "john"   #class variable
#     def __init__(self,name):    #local varibale amd parateterised constructor
#         print(name)
#         print(self.name)
# res=myclass("David")

#Example9:
# class myclass:
#     def __init__(self,eid,ename,salary):
#         self.eid = eid
#         self.ename = ename
#         self.salary = salary
#     def display(self):
#         print(self.eid,self.ename,self.salary)
#
# res=myclass(1144949,"John",14468)
# res.display()               #1144949 John 14468

#Example10: String constructor
class myclass:
    def __init__(self,eid,ename,salary):
        self.eid = eid
        self.ename = ename
        self.salary = salary
    def __str__(self):
        return (self.ename)

res=myclass("John")
print(res)          #John










