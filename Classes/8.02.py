# -*- coding: utf-8 -*-

"""
Classe Quadrado: crie uma classe que modele um quadrado:
a. Atributos; Tamanho do lado
b. Metodos: Mudar valor do lado, retornar valor do lado e calcular área.
"""

print("="*60)

class Quadrado():
	"""Cria uma classe quadrado"""

	def __init__(self, tamanho=''):
		"""Cria o tamanho do lado do quadrado."""
		self.tamanho = tamanho
		
	def mudarValor(self, novoValor=4):
		"""Muda o valor do lado do quadrado."""
		self.novoValor = novoValor
		print("O novo valor do lado e " + str(self.novoValor) + ".")

	def retornaValor(self):
		"""Retorna o valor do lado."""
		print("O valor do quadrado e " + str(self.novoValor) + ".")

	def calculaArea(self, area=4):
		"""Calcula a area do quadrado."""
		self.area = area**2
		print("A area do quadrado e " + str(self.area) + " .")

q = Quadrado(2)
print("O tamanho do quadrado e 2.")
q.mudarValor()
q.retornaValor()
q.calculaArea()


print("="*60)