# -*- coding: utf-8 -*-

"""
Faça um programa utilizando o módulo random de forma que o usuário
tenha três chances de acertar o número. O programa termina se o usuário
acertar ou errar três vezes.
"""

print(60 * "=")

import random

n = random.randint(1, 10)

for i in range(3):
    x = int(input("Escolha um número entre 1 e 10: "))

    if (x == n):
        print("Você acertou!")
    else:
        print("Você errou.")


print(60 * "=")
