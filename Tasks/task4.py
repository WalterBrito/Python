# Create a program that asks the user for a number and then prints out a list of
# all the divisors of that number. (If you don't know what a divisor is, it is a
# number that divides evenly into another number. For example, 13 is a divisor of
# 26 because 26 / 13 has no remainder.)

number = int(input("Type a number: "))
numberList = []

for i in range(1, number / 2):
    if number % i == 0:
        numberList.append(i)

print(numberList)
