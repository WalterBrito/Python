# Empty dictionary to store expenses and values to being pay
expensesNameValue = {}

# Get the user salary
salary = float(input("Enter the salary balance (ex: 1980.58 ): "))

# Loop info about user expanses
while True:
    # User enter the expenses and salary
    expenses = input("Enter the name os the expense (ex: bag): ").capitalize()
    expensesCharge = float(input("Enter the charge value (ex: 52.90): "))
    finish = input('Do you want exit? (y or n): ').lower()

    # Exit the program when user finished to enter expenses
    if finish == 'y':
        break

    if True:
        expensesNameValue[expenses] = expensesCharge
    else:
        print('What your type is not an valid option!\n Try again!')

print('========== Your Expenses ==========\n')
for key, value in expensesNameValue.items():
    print("{}: {}".format(key, value))
print('=' * 35)










