#Exapme1
# def fun(i,j):
#     print(i,j)
#
# fun(10,20)      #positional arguments
# fun(j=20,i=10)   #keyword arguments

#Example2: default value assigned to positional arguments

# def fun(i,j=10):
#     print(i,j)
#
# fun(20)      #default value to positional arguments

#Example3: Keyword arguments

# def greetings(name,message):
#     print(message+" "+name)
# greetings(message="hello",name="john")

#Example4:
def fun(a,b,c):
    print(a,b,c)
# fun(10,20,c=40)
# fun(10,c=20,b=100)
# fun(20,c=200,b=1)
# fun(a=10,20,20)     #positional argument follows keyword argument

#Example5: Function can return multiple values

def largest(a,b):
    if a>b:
        return a,b
    else:
        return b,a
print(largest(2,3))
