# -*- coding: utf-8 -*-

"""
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre
acidentes de trânsito. Foram obtidos os seguintes dados:
a. Código da cidade;
b. Número de veículos de passeio (em 1999);
c. Número de acidentes de trânsito com vítimas (em 1999).
Deseja-se saber:
d. Qual o maior e menor índice de acidentes de transito e a que
cidade pertence;
e. Qual a média de veículos nas cinco cidades juntas;
f. Qual a média de acidentes de trânsito nas cidades com menos de
2.000 veículos de passeio.
"""

print("==========================================================")

codigoCidade = int(input("Digite o codigo da cidade: "))
quantVeiculos = int(input("Digite o numero de veiculos na cidade: "))
quantAcidentes = int(input("Digite o numero de acidentes com vitimas da cidade: "))

indiceAcidente = float(quantAcidentes) / quantVeiculos
maiorIndice = indiceAcidente
maiorIndiceCodigo = codigoCidade
menorIndice = indiceAcidente
menorIndiceCodigo = codigoCidade
soma = quantVeiculos
somaVeiculos2000 = 0
divisorMedia2000 = 1

if quantVeiculos < 2000:
	somaVeiculos2000 = somaVeiculos2000 + quantAcidentes
	divisorMedia2000 += 1

i = 1
while i < 3:
	odigoCidade = int(input("Digite o codigo da cidade: "))
	quantVeiculos = int(input("Digite o numero de veiculos na cidade: "))
	quantAcidentes = int(input("Digite o numero de acidentes com vitimas da cidade: "))
	indiceAcidente = float(quantAcidentes) / quantVeiculos
	soma += quantVeiculos

	if indiceAcidente > maiorIndice:
		maiorIndice = indiceAcidente
		maiorIndiceCodigo = codigoCidade

	if indiceAcidente < menorIndice:
		menorIndice = indiceAcidente
		menorIndiceCodigo = codigoCidade

	if quantVeiculos < 2000:
		somaVeiculos2000 = somaVeiculos2000 + quantAcidentes
		divisorMedia2000 +=  1

	i += 1

print("\nMenor indice: %.2f Codigo da cidade: %d" % (menorIndice, menorIndiceCodigo))
print("\nMaior indice: %.2f Codigo da cidade: %d" % (maiorIndice, maiorIndiceCodigo))
print("Media de veiculos nas %d cidades = %d veiculos" % (i,(float(soma)/i)))
print("Media de acidentes em cidades com menos de 2000 veiculos: %.1f" % (float(somaVeiculos2000)/divisorMedia2000))

print("==========================================================")
