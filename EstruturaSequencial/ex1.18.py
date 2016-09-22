# -*- coding: utf-8 -*-

"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e
a velocidade de um link de Internet (em Mbps), calcule e informe o tempo
aproximado de download do arquivo usando este link (em minutos).
"""

print("============================================================")

arqTamanho = float(input("Digite o tamanho do arquivo (MB): "))
velocidadeLink = float(input("Digite a velocidade do link (Mbps): "))

tempoDownload = arqTamanho / (velocidadeLink * 60)

print("O tempo aproximado do download sera: %.2f minutos" % tempoDownload)


print("============================================================")
