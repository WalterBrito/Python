# -*- coding: utf-8 -*-

"""
Classe Retangulo: Crie uma classe que modele um retangulo:
a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e
Altura, a escolher)
b. Métodos: Mudar valor dos lados, Retornar valor dos lados,
calcular Área e calcular Perímetro;
c. Crie um programa que utilize esta classe. Ele deve pedir ao
usuário que informe as medidades de um local. Depois, deve criar
um objeto com as medidas e calcular a quantidade de pisos e de
rodapés necessárias para o local.
"""
print("="*60)

class Retangulo():
	"""Cria uma classe retangulo."""

	def __init__(self, comprimento='', largura=''):
		self.comprimento = comprimento
		self.largura = largura

	def mudaValorLado(self):
		"""Metodo que muda os valores do lado."""
		self.valorComprimento = int(input("Digite o valor do comprimento: "))
		self.valorLargura = int(input("Digite o valor da largura: "))

	def retornaValor(self):
		"""Retorna os valores dos lados."""
		print("\nO valor do comprimento e " + str(self.valorComprimento) + " cm².")
		print("O valor do largura e " + str(self.valorLargura) + " cm².")

	def calculaArea(self):
		"""Calcula a area dos lados."""
		self.area = self.valorComprimento * self.valorLargura
		print("A area do retangulo e " + str(self.area) + " cm².")

	def calculaPerimetro(self):
		"""Calcula a area dos perimetro."""
		self.perimetro = self.valorComprimento + self.valorLargura
		print("O perimetro do retangulo e " + str(self.perimetro) + " cm².\n")

retangulo = Retangulo()
retangulo.mudaValorLado()
retangulo.retornaValor()
retangulo.calculaArea()
retangulo.calculaPerimetro()

print("="*60)






