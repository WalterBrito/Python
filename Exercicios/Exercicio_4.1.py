# -*- coding: utf-8 -*-

"""
Escreva um programa que pergunte a velocidade do carro de um 
usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo
que o usuário foi multado. Nesse caso, exiba o valor da multa,
cobrando R$ 5 por km acima de 80 km/h.
"""

print(60 * "=")
velocCarro = int(input("Digite a velocidade do carro (Km): "))
velocPermitida = 80
multa = ((velocCarro - velocPermitida) * 5)

if velocCarro > velocPermitida:
    print("Você ultrapassou o limite permitido!")
    print("A multa é de R$ %.2f reais." % multa)
else:
    print("Você está dentro do limite permitido!")
print(60 * "=")
