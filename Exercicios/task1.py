# Create a program that asks the user to enter their name and their age. Print
# out a message addressed to them that tells them the year that they will turn
# 100 years old.

name = input("Type your name: ").capitalize()
age = int(input("Type your age: "))
birthday = int(input("Type your birthday: "))

yearNow = 2017
ageNow = (yearNow - birthday)
age100 = ((yearNow - age) + 100)
print("You have %d years old." % ageNow)
print("%s you will be 100 year old in %d." % (name, age100))
