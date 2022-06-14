#Exaple 1
# print("This is starting of the program")
# print("This is starting of the program")
# print("This is starting of the program")
# try:
#     print(x)
# except:
#     print("Exception Occured")
# print("This is Ending of the program")
# print("This is Ending of the program")
# print("This is Ending of the program")

#Example2
# print("This is starting point of the program")
# print("in progress")
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("Exception occured: Handled")
# print("program completed")

#Example3 : Multiple except blocks - try, except else, finally
# try:
#     num1,num2=10,10
#     result=num1/num2
#     print(result)
# except ZeroDivisionError:
#     print("Zero division error found")
# except SyntaxError:
#     print("Syntax error found")
# except:
#     print("some other error found")
# else:
#     print("No error found")
# finally:
#     print("always executes")

#Example4 : Raising our own exceptions
def enternum(num):
    if num<4:
        raise ValueError("number only less than 4 are allowed")

    if num%2==0:
            print("Even")
    else:
            print("Odd")
num=1
try:
    enternum(num)
except ValueError:
    print("Value error occured")
print("Program completed")









