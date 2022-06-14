#Factorial program
# num=5
# factorial = 1
# if num < 0:
#     print("factorial of negative number does not exist")
# elif num == 0:
#     print("factorial of 0 is 1")
# else:
#     for i in range (1,num+1):
#         factorial = factorial*i
#
# print(factorial)

#Fatorial through Recursion
# def factorial(n):
#     if (n<0 or n==0):
#         return 1
#     else:
#         return n * factorial(n-1)
#
# num=5
# print(factorial(num))

#factorial using ternary
# def factorial(n):
#     return 1 if (n<=0 or n==0) else n * factorial(n-1)
#
# num=5
# print(factorial(num))

#Fibonacci series
# n1 = 0
# n2 = 1
# num=10
# for i in range (1,num+1):
#     sum = n1 + n2
#     print(sum)
#     n1=n2
#     n2=sum

#Find elements in the List
# mylist=[1,2,4,5,6,7]
# # print(len(mylist))
# # count=0
# # for i in mylist:
# #     count = count+1
# # print(count)

#Find Max element in array
# mylist=[10,35,25,90,69,70]
# max=mylist[0]
# n=len(mylist)
#
# for i in range (1,n):
#     if mylist[i]>max:
#         max=mylist[i]
#
# print(max)

#Finding Min element in array
# mylist=[10,35,25,90,69,70]
# min=mylist[0]
# n=len(mylist)
# for i in range (1,n):
#     if mylist[i]<min:
#         min=mylist[i]
#
# print(min)

#factorial using for loop
# factorial = 1
# num = 5
#
# if (num < 1 or num == 0):
#     print("Factorial is 1")
# else:
#     for i in range (1,num+1):
#         factorial = factorial*i
#
#
# print(factorial)

#factorial using recursion
# def factorial(n):
#     if (n<0 or n==0):
#         return 1
#     else:
#         return n * factorial(n-1)
#
# num=5
# print(factorial(num))

#factorial using ternary

# def factorial(n):
#     return 1 if (n<0 or n==0) else n * factorial(n-1)
# print(factorial(5))

#Fibonacci series

# n1=0
# n2=1
#
# for i in range (1,10):
#     sum= n1+n2
#     print(sum)
#     n1=n2
#     n2=sum

#Finding prime number

# num=3
# count = 0
#
# for i in range (1,num+1):
#     if  (num % i == 0):
#         count = count + 1
# if count == 2:
#     print("number is prime")
# else:
#     print("number is not a prime")

#Sum of elements in array
# mylist=[1,2,3,4,5,6,7,8]
# print(sum(mylist,1))

#Swap first and last element using temp variable
# mylist=[12,34,54,13,90]
# temp=0
# n=len(mylist)
# temp=mylist[0]
# mylist[0]=mylist[n-1]
# mylist[n-1]=temp
# print(mylist)

#Swap without temporary variable
# mylist=[12,34,54,13,90]
#
# n=len(mylist)
# mylist[0],mylist[n-1]=mylist[n-1],mylist[0]
# print(mylist)

#using pop function
# mylist=[12,34,54,13,90]
# first=mylist.pop(0)
# last=mylist.pop(-1)
#
# mylist.insert(0,last)
# mylist.append(first)
#
# print(mylist)

#using * operand
# mylist = [12, 34, 54, 13, 90]
# first,*middle,last = mylist
# mylist=[last,middle,first]
# print(mylist)

#using tuple
# mylist = [12, 34, 54, 13, 90]
# get = (mylist[0],mylist[-1])
# (mylist[-1],mylist[-0])=get
# print(mylist)
































