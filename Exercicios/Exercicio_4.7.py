# -*- coding: utf-8 -*-

"""
Escreva um programa que calcule o preço a pagar  pelo fornecimento
de energia elétrica. Pergunte a quantidade de kWh consumida é o tipo
de instalação: R para residências, I para indústrias e C para comércios.
Calcule o preço a pagar de acordo com a tabela a seguir.

---------------------------------------------------------
| 			Preço por tipo e faixa de consumo			|
---------------------------------------------------------
|Tipo 		 |		Faixa (kWh)			|	  Preço     |
---------------------------------------------------------
|Residêncial |		Até 500				|	R$ 0,40		|
|Residêncial |		Acima 500			|	R$ 0,65		|
---------------------------------------------------------
|Comercial   |		Até 1000			|	R$ 0,55		|	
|Comercial   |		Acima 1000			|	R$ 0,60		|	
---------------------------------------------------------
|Industrial |		Até 5000			|	R$ 0,55		|
|Industrial |		Acima 5000			|	R$ 0,60		|
---------------------------------------------------------				

"""

print(60 * "=")

qntKwh = int(input("Qual a quantidade do consumo (kWh): "))
tipoInst = input("Digite (R - Residência), (C - Comércio), (I -Indústrias): ")


if qntKwh <= 500 and tipoInst == 'R':
    preço = qntKwh * 0.40
elif qntKwh > 500 and tipoInst == 'R':
    preço = qntKwh * 0.65
elif (qntKwh > 500 and qntKwh <= 100) and tipoInst == 'C':
    preço = qntKwh * 0.55
elif qntKwh > 1000 and tipoInst == 'C':
    preço = qntKwh * 0.60
elif (qntKwh > 1000 and qntKwh <= 5000) and tipoInst == 'I':
    preço = qntKwh * 0.55
elif qntKwh > 5000 and tipoInst == 'I':
    preço = qntKwh * 0.60
else:
    print("Inválido!")
    preço = 0

print("preço á pagar: R$ %.2f." % preço)

print(60 * "=")
