print("Welcome to my computer quiz!")
count = 0

playing=input("Do you want to Play? ")
if playing.lower() != "yes":
    quit()
else:
    print("Okay! Let's Play")
answer = input("What does CPU stands for? ").lower()
if answer == "central processing unit":
    print("Correct")
    count = count + 1
else:
    print("Incorrect :( ")
answer = input("What does GPU stands for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    count = count + 1
else:
    print("Incorrect :(")
answer = input("What does RAM stands for? ").lower()
if answer == "random access memory":
    print("Correct!")
    count = count + 1
else:
    print("Incorrect :(")

answer = input("What does ROM stands for? ").lower()
if answer == "read only memory":
    print("Correct!")
    count = count + 1
else:
    print("Incorrect :(")
answer = input("What does URL stands for? ").lower()
if answer == "uniform resource locator":
    print("Correct!")
    count = count + 1
else:
    print("Incorrect :(")


print("Your Score is "+str(count)+" out of 5")
print("Your got "+str((count / 5)*100)+"%")

