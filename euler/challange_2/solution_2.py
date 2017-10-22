evenF = [2]
number1 = 1
number2 = 2
nextNumber = 0

while number2 < 4000000:
    nextNumber = number1 + number2
    if nextNumber%2 == 0:
        evenF.append (nextNumber)
    number1 = number2
    number2 = nextNumber

sum = 0
for n in evenF:
    sum = (sum + n)

print (sum)