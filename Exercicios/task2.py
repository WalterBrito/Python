# Ask the user for a number. Depending on whether the number is even or odd, print
# out an appropriate message to the user.

num1 = int(input("Type first number: "))
check = int(input("Type second number: "))


if num1 % 4 == 0:
    print("The number is multiple of 4.")
elif num1 % 2 == 0:
    print("The number is even!")
else:
    print("The number is odd.")

