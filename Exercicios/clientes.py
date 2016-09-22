# -*-  coding: utf-8 -*-

# Classe clientes

print(60 * "=")


class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

joão = Cliente("João da Silva", "1234-5678")
maria = Cliente("Maria Silva", "5678-1234")

print(joão.nome)
print(joão.telefone)
print(maria.nome)
print(maria.telefone)

print(60 * "=")
