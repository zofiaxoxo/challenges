factors = []
primes = []
max_number = 13195

def isPrimeNumber(number):
    print (number)

for n in range (1 , max_number):
    if max_number % n == 0 :
        factors.append (n)

for x in factors:
    isPrimeNumber(x)

print (factors)
print (factors[0])


