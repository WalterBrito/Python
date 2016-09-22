# -*-  coding: utf-8 -*-

# Classe testes.py

print(60 * "=")

from clientes import Cliente
from conta import Conta

joão = Cliente("João da Silva", "1234-5678")
maria = Cliente("Maria Silva", "5678-1234")
josé = Cliente("José Silva", "6578-2134")

conta1 = Conta([joão], 1, 1000)
conta2 = Conta([maria, joão], 2, 500)
conta3 = Conta([joão, maria, josé], 3, 5000)
conta1.saque(5000)
conta2.deposito(300)
conta3.deposito(500)
conta1.saque(190)
conta2.deposito(95.15)
conta2.deposito(250)
conta3.deposito(150)
conta1.extrato()
conta2.extrato()
conta3.extrato()

print(60 * "=")
