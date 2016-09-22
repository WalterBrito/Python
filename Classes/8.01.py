# -*- coding: utf-8 -*-

"""
Classe Bola: Crie uma classe que modele uma bola:
a. Atributos: Cor, circunferência, material
b. Métodos: trocaCor e mostraCor
"""

print("="*60)

class Bola():
	"Cria uma classe bola."

	def __init__(self, cor='azul', circunferencia='redonda', material='plastico'):
		self.cor = cor 
		self.circunferencia = circunferencia
		self.material = material

	def trocaCor(self, novaCor='verde'):
		""" Metodo que troca a cor."""
		self.novaCor = novaCor	
		print("A cor foi trocada para " + self.novaCor.title() + ".\n")	
		
	def mostraCor(self):
		""" Metodo que mostra cor, circunferencia e material."""
		print("A cor original e " + self.cor.title() + ".")
		print("A bola e " + self.circunferencia.title() + ".")
		print("A bola e feita de " + self.material.title() + ".")


bola = Bola('azul', 'redonda', 'plastico')
bola.trocaCor()
bola.mostraCor()

print("="*60)