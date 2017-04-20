# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers
# and the square of the sum is 3025 - 385 = 2040. Find the difference between the sum of
# the squares of the first one hundred natural numbers and the square of the sum.

sumSquare = []
squareSum = []
for i in range(1, 101):
    if i ** 2:
        squareSum.append(i ** 2)
        # add sum of the square to the list
        sumSquare.append(i)
# Sum of the squares of the first one hundred numbers
print("Sum of the square:", sum(squareSum))
# square of the sum of the first one hundred numbers
print("Square of the sum:", sum(sumSquare) ** 2)
# Difference between the sum of the squares of the first one hundred numbers
print("Difference: ", (sum(sumSquare) ** 2) - sum(squareSum))