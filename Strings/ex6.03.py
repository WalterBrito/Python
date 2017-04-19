# -*- coding: utf-8 -*- 

"""
'''Nome na vertical.''' Faça um programa que solicite o nome do usuário e
imprima-o na vertical.
F 
U 
L
A
N 
O 
"""

print("=======================================================")

nome = input("Digite seu nome: ").capitalize()

i = 0
while i <= len(nome):
	print(nome[i:i+1])
	i += 1

print("=======================================================")