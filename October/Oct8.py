def makelist(number):
    newlst = []
    for i in range(number):
        newlst.append(i)
    return newlst

def rocketcountdown(countdown):
    newlst = []
    for i in range(countdown, 0, -1):
        newlst.append(i)
    newlst.append('We have lift off!')
    return newlst

def doubleloop(len1,len2):
    newlst = []
    for i in range(len1):
        for j in range(len2):
            newlst.append(f'{i}:{j}')
    return newlst

def howmanycombos(l1, l2, l3):
    newlst = []
    for i in range(l1+1):
        for j in range(l2+1):
            for k in range(l3+1):
                newlst.append(f'{i}:{j}:{k}')
    return newlst

def cansofpop(number, takedown):
    newlst = []
    while number > 0:
        if number - takedown < 0:
            takedown = number
        newlst.append(f'{number} cans of pop on the wall {number} cans of pop, take {takedown} down and pass them around, {number-takedown} cans of pop on the wall')
        number -= takedown
    newlst.append('All cans of pop are gone!')
    return newlst

def main():
    '''
    This is where you can write your own tests for your methods!
    '''
    print(cansofpop(10, 3))
    return

if __name__ == '__main__':
    main()