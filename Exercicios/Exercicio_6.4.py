# -*- coding: utf-8 -*-

"""
Faça um programa que leia uma expressão com parênteses. Usando pilhas,
verifique se os parênteses foram abertos e fechados na ordem correta.
Exemplo:

(())        OK
()()(()())  OK
())         OK
"""

print(60 * "=")

expressão = input("Digite a sequência de parênteses a validar: ")
x = 0

pilha = []

while x < len(expressão):

    if (expressão[x] == "("):
        pilha.append("(")
    if (expressão[x] == ")"):
        if (len(pilha) > 0):
            topo = pilha.pop(-1)
        else:
            pilha.append(")")  # Força a mensagem de erro
            break
    x += 1

if (len(pilha) == 0):
    print("OK")
else:
    print("Erro")

print(60 * "=")
