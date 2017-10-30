counter = 0
numberFound = True
x = 0

def isNumberFound (number):
    for x in range (2, 20):
        if number % x != 0:
            return False
        return True




while numberFound:
    counter = counter + 1
    if isNumberFound(counter):
        print (counter)
        numberFound = False