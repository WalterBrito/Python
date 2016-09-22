# -*- coding: utf-8 -*-

"""
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita
a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"
As possíveis respostas são:
1-Windows Server
2-Unix
3-Linux
4-Netware
5-Mac OS
6-Outro

Você foi contratado para desenvolver um programa que leia o
resultado da enquete e informe ao final o resultado da mesma. O
programa deverá ler os valores até ser informado o valor 0, que
encerra a entrada dos dados. Não deverão ser aceitos valores além
dos válidos para o programa (0 a 6). Os valores referentes a cada
uma das opções devem ser armazenados num vetor.
Após os dados terem sido completamente informados, o programa deverá
calcular a percentual de cada um dos concorrentes e informar o
vencedor da enquete. O formato da saída foi dado pela empresa, e é o
seguinte:
Sistema Operacional			Votos    %
-------------------			-----	---
Windows Server 				1500	17%
Unix						3500	40%
Linux						3000	34%
Netware						 500	 5%
Mac OS						 150	 2%
Outro						 150	 2%
-------------------			-----
Total						8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos,
correspondendo a 40%  dos votos.
"""

print("========================================================")

print("Qual o melhor Sistema Operacional para uso em servidores?\n\n")
print("As possiveis respostas são: \n")
print("1-Windows Server\n2-Unix\n3-Linux\n4-Netware\n5-Mac OS\n6-Outros")

votos = [1]
while votos[len(votos)-1] != 0:
	voto = input("Digite seu voto: ")
	if voto <= 6:
		votos.append(voto)
	else:
		print("Voto invalido! tente outra vez.")

votos.pop(0)
votos.pop(len(votos)-1)

votosWindows = votos.count(1)
votosUnix = votos.count(2)
votosLinux = votos.count(3)
votosNetware = votos.count(4)
votosMacOS = votos.count(5)
votosOutros = votos.count(6)

total = votosWindows + votosUnix + votosLinux + votosNetware + votosMacOS + votosOutros

porcWindows = (float(votosWindows)/(len(votos))) * 100
porcUnix    = (float(votosUnix)/(len(votos))) * 100
porcLinux 	= (float(votosLinux)/(len(votos))) * 100
porcNetware = (float(votosNetware)/(len(votos))) * 100
porcMacOS   = (float(votosMacOS)/(len(votos))) * 100
porcOutros  = (float(votosOutros)/(len(votos))) * 100

print("Sistema Operacional				Votos 			 	Porcentagem")
print("Windows Server 					", votosWindows," 		','		""%(#)0.2f%%" % {"#" : porcWindows})
print("Unix 							", votosUnix," 			','		""%(#)0.2f%%" % {"#" : porcUnix})
print("Linux 							", votosLinux," 		','		""%(#)0.2f%%" % {"#" : porcLinux})
print("Netware							", votosNetware," 		','		""%(#)0.2f%%" % {"#" : porcNetware})
print("Mac OS							", votosMacOS," 		','		""%(#)0.2f%%" % {"#" : porcMacOS})
print("Outros							", votosOutros," 		','		""%(#)0.2f%%" % {"#" : porcOutros})
print("\n")
print("Total: ", total)

print("========================================================")