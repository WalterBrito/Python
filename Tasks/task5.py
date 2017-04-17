# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
# 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
#

def sumMultiples():
    result = 0
    # iterate 0 until 1000
    for i in range(1001):
        # Append multiple of 3 in multiple3
        if not (i % 3) or not (i % 5):
            result += i
    print("Sum: %d" % result)

sumMultiples()