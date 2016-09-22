# -*- coding: utf-8 -*-

# Obtenção do preco utilizando dicionarios.

print("======================================================")

tabela = {"Alface": 0.45,
		  "Batata": 1.20,
		  "Tomate": 2.30,
		  "Feijao": 1.50 }

while True:
	produto = input("Digite o nome do produto (s para sair): ")
	if produto == "s":
		break
	if produto in tabela:
		print("Preco %.2f." % tabela[produto])
	else:
		print("Produto nao encontrado!")

print("======================================================")