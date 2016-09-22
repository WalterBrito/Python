# -*- coding: utf-8 -*-

"""
Escreva um programa que leia um número e verifique se é
ou não um número primo. Para fazer essa verificação, calcule
o resto da divsão do número por 2 e depois por todos os números 
impares até o número lido. Se o resto de uma dessas divisões for
igual a zero, o número não é primo. Observe que o 0 e 1 não são 
primos e que 2 é o único número primo que é par.
"""

print(60 * "=")

num = int(input("Digite um número: "))

if num < 0:
    print("Número Inválido. Somente valores positivos.")
if num == 0 or num == 1:
    print("$=%d é um caso especial." % num)
else:
    if num == 2:
        print("2 é primo!")
    elif num % 2 == 0:
        print("O número %d não é primo!" % num)
    else:
        x = 3
        while (x < num):
            if num % x == 0:
                break
            x += 2
        if x == num:
            print("O número %d é primo!" % num)
        else:
            print("%d não é primo, pois é divisivel por %d" % (num, x))

print(60 * "=")
