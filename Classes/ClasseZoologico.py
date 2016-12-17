#-*- coding: utf-8 -*-

class Zoologico():

    def __init__(self, nome, especie, cor):
        self.nome = nome
        self.especie = especie
        self.cor = cor

    def animal(self):
        print("O nome do animal é " + self.nome + ".")
        print("A especie do animal é " + self.especie + ".")
        print("A cor do animal é " + self.cor + ".")

a = Zoologico("Simbá", "Mamifero", "Amarelo")
a.animal()
