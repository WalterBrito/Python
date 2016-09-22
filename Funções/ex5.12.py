# -*- coding: utf-8 -*-

"""
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço
em disco no seu servidor de arquivos. Para tentar resolver este problema, o
Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e
identificar os usuários com maior espaço ocupado. Através de um programa,
baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado
"usuarios.txt":
alexandre 		456123789
anderson		1245698456
antonio			123456456
carlos			91257581
cesar			987458
rosemary		789456125

	Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste
arquivo, você deve criar um programa que gere um relatório, chamado
"relatório.txt", no seguinte formato:

ACME Inc. 				Uso do espaço em disco pelos usuários
----------------------------------------------------------------------
--
Nr. Usuário 		Espaço utilizado	%  do uso

1 alexandre			434,99  MB			16,85%
2 anderson			1187,99	MB			46,02%
3 antonio			117,73	MB			4,56%
4 carlos			87,03	MB			3,37%
5 cesar				0,94	MB			0,04%
6 rosemary			752,88	MB			29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB

	O arquivo de entrada deve ser lido uma única vez, e os dados
armazenados em memória, caso sejam necessários, de forma a agilizar a
execução do programa. A conversão da espaço ocupado em disco, de bytes
para megabytes deverá ser feita através de uma função separada, que
será chamada pelo programa principal. O cálculo do percentual de uso
também deverá ser feito através de uma função, que será chamada pelo
programa principal.
"""

print("======================================================")

dic = {}

# Conversao para MB
def totalMB(bytes):
	return float(bytes/1024)

# Calculo porcentagem
def porcentagem(bytes, total):
	return float(totalMB(bytes)*100/totalMB(total))

# Calculo media
def calcMedia(bytes, totalArquivo):
	return float(totalMB(bytes)/totalArquivo)  # Erro

# Trazendo arquivo
filename = "usuarios.txt"
f = open(filename, 'r')
todasLinhas = f.readlines()
f.close()

# Montando dicionario de dados
espacoTotal, totalArquivo = 0, 0

for l in todasLinhas:
	nome = l[:16]
	use = int(l[16:])
	dic[nome]=use
	espacoTotal += use
	totalArquivo += 1

# Gerando o relatorio

print("ACME Inc. 				Uso do espaço em disco pelos usuários")
print("----------------------------------------------------------------------")
print("Nr. Usuário \t\tEspaço utilizado\t%  do uso")

i = 0
for k, v in dic.items():
	print(i," ",k,"\t",totalArquivo(v)," MB\t\t"+str(porcentagem(v, espacoTotal))+"%")
print("Espaco total ocupado: ", (totalArquivo+(espacoTotal))," MB")  # Erro
print("Espaco medio ocupado: ", calcMedia(espacoTotal, totalArquivo), " MB")

print("======================================================")