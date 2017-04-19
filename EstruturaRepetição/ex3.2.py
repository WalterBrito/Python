# -*- coding: utf-8 -*-

"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha
igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as
informações.
"""


print("=======================================================")

while True:
	nome = input("Digite seu nome de usuário: ")
	senha = input("Digite sua senha: ")

	if senha != nome:
		print("Seu nome de usuario: %s" % nome)
		print("Sua senha: %s" % senha)
		break
	else:
		print("Invalido! tente outra vez.")


print("=======================================================")
