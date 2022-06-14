#How to Find Factorial of a number
#num=5
#1 * 2 * 3 * 4 * 5 = 120

#Approach1: Iterative
# factorial = 1
# num=0
#
# if num<0:
#     print("Factorial does not exist for negatvie numbers ")
# elif num==0:
#     print("Factorial of 0 is 1 ")
# else:
#     for i in range (1,num+1):
#         factorial = factorial*i
#
# print("Factorial of",num,"is",factorial)

#Approach2: Recursion
# def factorial(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)
#
# num=8
# print("Factorial of",num,"is",factorial(num))

#Approach3: Ternary
# def factorial(n):
#     return 1 if (n==0 or n==1) else n*factorial(n-1)
#
# num=8
# print("Factorial of",num,"is",factorial(num))   #40320
