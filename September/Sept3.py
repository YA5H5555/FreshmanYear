## Lab 01 - ALl About Functions
##
## This lab is to get you help you learn all about functions! You will learn
## how to define a function, call a function, return values from a function,
## and parameters in a function.


# STEP 1
def printStatement():
    print("Welcome to your second lab!")
    print('This is my first print statement!')


# STEPS 2&3
def returnValues():
    return "This is my first return statement!"


# STEP 4
def parameters(num1,num2):
    multiplication = num1 * num2
    return multiplication


# STEP 5
# define your function here
def iceCreamOrder():
    cost =int(6)
    flavor = str(input("What flavor would you like? => "))
    return "The " + flavor + " will cost " + str(cost) + " dollars."

def run():
    printStatement()
    print(returnValues())
    print(parameters(1,4))
    print(parameters(5,7))
    print(iceCreamOrder())
    return #Do NOT change anything in this line!
    
if __name__ == '__main__':
    run()
