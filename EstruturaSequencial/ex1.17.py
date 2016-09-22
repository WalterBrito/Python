# -*- coding: utf-8 -*-

"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho
em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é
de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18
litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os
respectivos preços em 3 situações:
a. comprar apenas latas de 18 litros;
b. comprar apenas galões de 3,6 litros;
c. misturar latas e galões, de forma que o preço seja o menor.
"""

print("=======================================================")


area = input('Digite o tamanho da area (Metros): ') # Pedir a area ao utilizador

litros = 18.0 
galoes = 3.6 
precoLitro = 80.0 
precoGaloes = 25.0 
areaLitroTinta = 6.0 

tintaNecessaria = area/areaLitroTinta # Litros de tinta necessarios para a pintura

if tintaNecessaria == 1:
    print('Vai precisar de um litro de tinta.')
elif tintaNecessaria != 1 and tintaNecessaria > 0:
    print('Vai precisar de %d litros de tinta' % tintaNecessaria)
else:
    print('Ivalido! tente outra vez.')
   

litrosNecessario = tintaNecessaria/litros # Devolve a qtdade de litros necessarias para pintar a area prentendida

restanteTinta = tintaNecessaria%litros # Devolve a qtd de tinta que fica em excesso dos litros.

# Com base nesse excesso, vemos se o que e usado da ultima lata justifica a sua compra
# Temos o valor excessivo a partir de (3.6*4) porque e o valor em que as latas pequenas ficam mais caras que uma grande
if litros - restanteTinta < (3.6*4):
    galoesNecessario = (litros - restanteTinta) / galoes

# Devolve o preco da mistura (litros e galoes)

if galoesNecessario != 0:
    precoFinal = (precoLitro * (int(litrosNecessario)-1)) + ((int(galoesNecessario)) * precoGaloes)
else:
    precoFinal = precoLitro * int(litrosNecessario)

print('Preco final: %.2f' % precoFinal)
print('Preco em litros: %.2f' % (litrosNecessario * precoLitro))
print('Preco em galoes: %.2f' % (precoGaloes * (tintaNecessaria / galoes)))

print("=======================================================")
