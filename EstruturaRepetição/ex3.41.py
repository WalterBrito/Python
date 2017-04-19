# -*- coding: utf-8 -*-

"""
Desenvolver um programa para verificar a nota do aluno em uma prova com 10
questões, o programa deve perguntar ao aluno a resposta de cada questão e ao
final comparar com o gabarito da prova e assim calcular o total de acertos e a nota
(atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser
feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos
terem respondido informar:
a. Maior e Menor Acerto;
b. Total de Alunos que utilizaram o sistema;
c. A Média das Notas da Turma.
Gabarito da Prova:
01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
	Após concluir isto você poderia incrementar o programa permitindo
que o professor digite o gabarito da prova antes dos alunos usarem o
programa.
"""

print("===========================================================")

# Gabarito
gab01 = "a"
gab02 = "b"
gab03 = "c"
gab04 = "d"
gab05 = "e"
gab06 = "e"
gab07 = "d"
gab08 = "c"
gab09 = "b"
gab10 = "a"

# Fim do gabarito
soma = 0
maiorAcerto = -1
menorAcerto = 11
final = 1
i = 1
somaMedia = 0

while final == 1:
	resposta01 = input("Digite a resposta da questao 1: ")
	if resposta01 == gab01:
		soma += 1

	resposta02 = input("Digite a resposta da questao 2: ")
	if resposta02 == gab02:
		soma += 1
		
	resposta03 = input("Digite a resposta da questao 3: ")
	if resposta03 == gab03:
		soma += 1
		
	resposta04 = input("Digite a resposta da questao 4: ")		
	if resposta04 == gab04:
		soma += 1
		
	resposta05 = input("Digite a resposta da questao 5: ")
	if resposta05 == gab05:
		soma += 1
		
	resposta06 = input("Digite a resposta da questao 6: ")
	if resposta06 == gab06:
		soma += 1		

	resposta07 = input("Digite a resposta da questao 7: ")		
	if resposta07 == gab07:
		soma += 1
		
	resposta08 = input("Digite a resposta da questao 8: ")
	if resposta08 == gab08:
		soma += 1
		
	resposta09 = input("Digite a resposta da questao 9: ")
	if resposta09 == gab09:
		soma += 1
		
	resposta10 = input("Digite a resposta da questao 10: ")
	if resposta10 == gab10:
		soma += 1		

	if soma > maiorAcerto:
		maiorAcerto = soma

	if soma < menorAcerto:
		menorAcerto = soma

	somaMedia = float(somaMedia + soma)

	final = int(input("(1) Para outro aluno responder (0) para finalizar: "))
	i += 1
	soma = 0

print("Maior numeros de acertos: %d" % maiorAcerto)
print("Menor numeros de acertos: %d" % menorAcerto)
print("Alunos que usaram o sistema: %d" % (i - 1))
print("Media das notas: %.1f" % (somaMedia / (i - 1)))

print("===========================================================")
