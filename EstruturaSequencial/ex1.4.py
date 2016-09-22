# -*- coding: UTF-8 -*-

# Faça um Programa que peça dois números e imprima a soma.

print('===============================================')

nota1 = int(input("Digite a 1 nota: "))
nota2 = int(input("Digite a 2 nota: "))
nota3 = int(input("Digite a 3 nota: "))
nota4 = int(input("Digite a 4 nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
	print("A media e: %.1f" % media)
	print("Aluno aprovado!")
else:
	print("A media e: %.1f" % media)
	print("Aluno reprovado!")

print('===============================================')
