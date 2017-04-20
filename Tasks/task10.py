# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def sumPrimes(n):
    if n < 2: return "Neither prime, nor composite"
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

sumAll = 0
for i in range(2, 2000000):
    if sumPrimes(i):
        sumAll += i
print("Sum of all the primes: %d" % sumAll)