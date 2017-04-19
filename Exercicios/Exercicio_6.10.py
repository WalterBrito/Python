# -*- coding: utf-8 -*-

"""
Faça um progra com esqtoque e opeção de vendas. O programa
deve solicitar ao usuário o produto e a quantidade vendida. 
Verifique se o nome do produto digitado existe no dicionário,
e só então efetue  a baixa em estoque.
"""

print(60 * "=")

estoque={ "tomate": [ 1000, 2.30],
          "alface": [   500, 0.45],
          "batata": [ 2001, 1.20],
          "feijão": [   100, 1.50] }
venda = [ ["tomate", 5], ["batata", 10], ["alface",5]]
total = 0
print("Vendas:\n")
while True:
    produto =  input("Nome do produto (fim para sair): ")

    if produto == "fim":
        break 
    if produto in estoque:
        quantidade = int(input("Quantidade: "))

        if quantidade <= estoque[produto][0]:
            preço = estoque[produto][1]
            custo = preço * quantidade 
            print("%12s: %3d x %6.2f = %6.2f" % (produto, quantidade,
                                                preço, custo))
            estoque[produto][0] -= quantidade
            total += custo 
        else:
            print("Quantidade solicitada não disponivel")
    else:
        print("Nome do produto inválido") 

print(" Custo total: %21.2f\n" % total)
print("Estoque:\n")
for chave, dados in estoque.items():
     print("Descrição: ", chave)
     print("Quantidade: ", dados[0])
     print("Preço: %6.2f\n" % dados[1])

print(60 * "=")