# -*- coding: utf-8 -*-


"""
Escreva um programa para controlar uma pequena máquina
registradora. Você deve solicitar ao usuário que digite
o código do produto e a quantidade comprada. Utilize
a tabela de códigos abaixo para obter o preço  de cada
de cada produto:
-----------------------
|  Código |	  Preço   |	
|	1	  |   0,50    |
|	2	  |   1,00    |
|	3	  |   4,00    |
|	5	  |   7,00    |
|	9	  |   8,00    |
-----------------------

Seu programa deve exibir o total de compras depois que o 
usuário digitar 0. Qualquer outro código deve gerar a 
mensagem de erro "Código inválido".
"""

print(60 * "=")


x = 0
soma = 0
while True:
    codProd = int(input("Digite o código do produto: "))

    if codProd == 0:
        break
    if codProd == 1:
        preço = 0.50
    elif codProd == 2:
        preço = 1.00
    elif codProd == 3:
        preço = 4.00
    elif codProd == 5:
        preço = 7.00
    elif codProd == 9:
        preço = 8.00
    else:
        print("Código inválido")
    qntCompra = int(input("Digite a quantidade de produto(s): "))
    x += qntCompra
    soma = soma + (qntCompra * preço)

print("%d produto(s) comprado(s)!" % x)
print("Total de compras: R$ %.2f " % soma)

print(60 * "=")
