# -*- coding: utf-8 -*-

"""
Faça um programa de forma que se possa trabalhar com vários
comandos digitados de uma só vez. Atualmente, apenas um comando
pode ser inserido por vez. Altere-o de forma a considerar operação
como uma string.

Exemplo: FFFAAAS significaria três novos clientes, três novos
atendimentos e, finalmente, a saida do programa.
"""

print(60 * "=")

último = 10
fila = list(range(1, último + 1))
while True:
    print("\nExistem %d clientes na fila" % len(fila))
    print("Fila atual:", fila)
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operação = input("Operação (F, A ou S):")
    x = 0
    sair = False

    while x < len(operação):
        if operação == "A" or operação == "a":
            if(len(fila)) > 0:
                atendido = fila.pop(0)
                print("Cliente %d atendido" % atendido)
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operação == "F" or operação == "f":
            último += 1  # Increnta o ticket do novo cliente
            fila.append(último)
        elif operação == "S" or operação == "s":
            sair = True
            break
        else:
            print("Operação inválida: %s na posição %d! Digite apenas F, A ou S!" % (operação, [x], x))
        x += 1
    if (sair):
        break    
                
print(60 * "=")
