# -*- coding: utf-8 -*-

"""
Faça um programa que leia e valide as seguintes informações:
a.Nome: maior que 3 caracteres;
b.Idade: entre 0 e 150;
c.Salário: maior que zero;
d.Sexo: 'f' ou 'm';
e.Estado Civil: 's', 'c', 'v', 'd';
"""

print("=========================================================")

for i in range(4):
	nome = input("Qual o seu nome: ")
	idade = int(input("Qual sua idade (0 a 150): "))
	salario = float(input("Qual valor do seu salario?: "))
	sexo = input("Qual seu sexo (M-Masculino / F-Feminino)?: ")
	estCivil = input("Qual seu estado civil? 's', 'c', 'v', 'd': ")

	if len(nome) > (3):
		print("Seu nome: %s" % nome)
	else:
		print("Nome invalido!")

	if idade > 0 and idade <= 150:
		print("Sua idade: %d anos." % idade)
	else:
		print("Idade invalida!")

	if salario > 0:
		print("O valor do salario: %.2f" % salario)
	else:
		print("Valor do salario invalido.")

	if sexo == "M" or sexo == "m":
		print("Seu sexo e Masculino!")
	elif sexo == "F" or sexo == "f":
		print("Seu sexo e Feminino!")
	else:
		print("Sexo invalido!")

	if estCivil == "S" or estCivil == "s":
		print("Voce e Solteiro(a)!")
	elif estCivil == "C" or estCivil == "c":
		print("Voce e Casado(a)!")
	elif estCivil == "V" or estCivil == "v":
		print("Voce e Viuvo(a)!")
	elif estCivil == "D" or estCivil == "d":
		print("Voce e Divorciado(a)!")
	else:
		print("Estado Civil invalido!")
	break


print("=========================================================")
