# -*- coding: utf-8 -*-

"""
Escreva um programa que leia números inteiros do teclado. 
O programa deve ler os números até que o usuário digite 0
(zero). No final da execução exiba a quantidade de números
digitados, assim como a soma e a média aritmética.
"""

print(60 * "=")

qntDigitados = 0
soma = 0

while True:
    n = int(input("Digite um número ou 0 para sair: "))

    if n == 0:
        break

    qntDigitados += 1  				
    soma += n 		   				
    média = soma / qntDigitados	 	


print("\nQuantidade de números digitados: %d " % qntDigitados)
print("A soma dos números: %d" % soma)
print("A média dos números: %.1f" % média)

print(60 * "=")
