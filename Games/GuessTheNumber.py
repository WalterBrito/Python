# -*- coding: utf-8 -*-
# This is a Guess the number game.
import random
import text

guessesTaken = 0
myName = input("Hello! What's  your name?: ").capitalize()

number = random.randint(1, 20)
print("Well, " + myName + ", I am thinking of a number between 1 and 20.")

while guessesTaken < 6:
    print('Take a guess: ') # There are four spaces in front of print
    guess = int(input('Type a number (1 - 20): '))
    guessesTaken += 1

    if guess < number:
        print('Your guess is too low.') # There are eight spaces in front of print.
    if guess > number:
        print('Your guess is too high.')
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in '
         + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)





















