min = 100
max = 1000
maxPalidromic = 0

def palindromicNumber(number):
    reverse = str(number)[::-1]
    if reverse == str(number):
        return True
    else:
        return False


for a in range (min, max):
    for b in range (min, max):
        c = (a * b)
        if palindromicNumber(c):
            if maxPalidromic < c:
                maxPalidromic = c

print (maxPalidromic)