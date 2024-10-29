def factorial(num1):
    total = 1
    while (num1>0):
        total = total * num1
        num1 -= 1
    return total

def moduloPractice(num1):
    return num1 % 9

def evenNum(num1):
    if num1 % 2 == 0:
        return True
    else:
        return False
    return None

def oddNum(num1):
    if num1 % 2 != 0:
        return True
    else:
        return False
    return None

def checkNum(num1):
    if evenNum(num1) == True:
        return "even"
    else:
        return "odd"
    return None

def run():
    num1 = int(input())
    print("Factorial:",factorial(num1))
    print("Modulo:",moduloPractice(num1))
    print("Even:",evenNum(num1))
    print("Odd:",oddNum(num1))
    print("Even or Odd:",checkNum(num1))

if __name__ == '__main__':
    print()
    run()