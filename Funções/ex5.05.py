# -*- coding: utf-8 -*-

"""
Faça um programa que converta da notação de 24 horas para a notação de 12
horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é
dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a
conversão e uma para a saída. Registre a informação A.M./P.M. como um valor
‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um
parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita
que o usuário repita esse cálculo para novos valores de entrada todas as vezes que
desejar.
"""

print("==========================================================")

def converteHora(hh, mm):
    if hh > 12:
        return hh - 12
    elif hh == 0:
        return 12
    else:
        return hh
 
def printHora(hh, mm):
    if hh >= 12:
        print(str(converteHora(hh,mm))+":"+str(mm)+" PM")
    elif hh == 0:
        print("12:"+str(mm)+" AM")
    else:
        print(str(hh)+":"+str(mm)+" AM")
 
i = 0
while i != 1:
    print("\nConversor de hora\n")
    # No python 3 apresenta erro, so funciona com o raw_input
    hora = raw_input("digite a hora que deseja converter de 24 para 12h (hh:mm): ") 
    hh = int(hora[0:2])
    mm = hora[3:5]
    print "\n"
    printHora(hh,mm)
    i = int(input("\nDigite 0 para conitnuar ou 1 para sair:  "))
    while i != 0 and i != 1:
            i = int(input("\nDigite 0 para conitnuar ou 1 para sair: "))
    if i == 1:
        print("\n Ate a proxima!!")

print("==========================================================")