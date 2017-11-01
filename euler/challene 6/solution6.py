sumOfSquares = 0
sumOfNumbers = 0
maxNumber = 100

for x in range (1, maxNumber + 1):
    sumOfSquares += (x * x)

for n in range (1, maxNumber + 1):
    sumOfNumbers += n

square = sumOfNumbers * sumOfNumbers

print (square - sumOfSquares)