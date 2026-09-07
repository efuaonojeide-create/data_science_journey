#Exception
'''
number = 2
assert(number<5),f"The number should not exceed 5.({number =})"
print (number)
'''
'''
def linux_interaction():
    import sys
    if "Linux" not in sys.platform:
        raise RuntimeError("Function can only run on Linux systems.")
    print("Doing Linux things.")

try:
    linux_interaction()
except RuntimeError as error:0
    print(error)
    print("The linux_interaction() function wasn't executed.")
'''
'''
try:
    with open ("Tracker.csv") as file:
        read_data = file.read()
except FileNotFoundError as E:
    print (E)
'''
#Wednesday's Warm up
'''
try:
    print (0/0)
except ZeroDivisionError as E:
    print (E)
'''
#Leap year calculator from Phase 1
'''
try:
    N = int(input("Insert a number: "))

    if (N %4==0 and N %100 !=0) or (N%4== 0 and N%100 == 0 and N%400 == 0):
        print ("it's a leap year!") 
    elif (N%4 != 0) or (N%4==0 and N%100 == 0 and N%400 != 0):
        print ("It's not a leap year!")
except ValueError:
    print ("This isn't a number!")
'''

#Wednesday's Core
'''
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

while True:
    print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Quit")
    choice = input("Choose an option: ")

    if choice == "5":
        print("Goodbye!")
        break

    try:

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", add(num1, num2))
        elif choice == "2":
            print("Result:", subtract(num1, num2))
        elif choice == "3":
            print("Result:", multiply(num1, num2))
        elif choice == "4":
            print("Result:", divide(num1, num2))
        else:
            print("Invalid choice, try again.")
    except ValueError:
        print ("This  isn't a number!")
    except ZeroDivisionError:
        print ("Can't divide by Zero!")
'''

#Wednesday's Challenge
def File():

    file_name = input("What file do you want:")
    try:
        with open (f"{file_name}") as f:
            read_data = f.read()
    except FileNotFoundError:
        print ("File doesn't exist!")

File()