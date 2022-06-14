#Example1
# global_var=20       #global variable
#
# def fun():
#     local_var=10
#     print(local_var)
#     print(global_var)
#
# fun()
#
# #print(local_var)    #local variable cannot be accessed autside the function
# print(global_var)

#Example2:
# xy=100
# def cool():
#     xy=200
#     print(xy)
# cool()
#
# print(xy)

#Example3
# xy=100
# def cool():
#     #global xy=200      #Invalid statement
#     global xy
#     xy=200      #global variable
#     print(xy)
# cool()
#
# print(xy)

#Example4
x=100

def cool():
    global x
    x=500
    print(x)
#cool()
print(x)