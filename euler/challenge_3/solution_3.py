factors = []
primes = []
max_number = 600851475143

def isPrimeNumber(number):
    for z in range (2, int(number / 2 )):
        if number % z == 0:
           return False
    return True


for n in range(1 , int(max_number / 2)):
    if n % 100000000 == 0:
        print ("....." + str(n) + " no of factors found so far: " + str(len(factors)))
    if max_number % n == 0:
        factors.append (n)
print ("finished factors")
print (len(factors))

for x in factors:
    if isPrimeNumber(x):
        print (x)

# 6857
