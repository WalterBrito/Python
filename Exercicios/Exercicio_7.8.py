# -*- coding: utf-8 -*-

"""
Jogo da forca 
Modifique o jogo da forca de forma a utilizar uma lista de palavras.
No inicio, pergunte um número e calcule o indice da palavra a utilizar
pela fórmula:

indice = (número * 776) %  len(lista_de_palavras)
"""

print()

palavras = [
    "casa",
    "bola",
    "mangueira",
    "uva",
    "quiabo",
    "computador",
    "cobra",
    "lentilha",
    "arroz"
]

indice = int(input("Digite um número: "))
palavra = palavras[(indice * 776) % len(palavras)]

for x in range(100):
    print()

digitadas = []
acertos = []
erros = 0

while True:

    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)

    if senha == palavra:
        print("Você acertou!")
        break
    tentativa = input("\nDigite uma letra: ").lower().strip()

    if tentativa in digitadas:
        print("Você já tentou está letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
    print("X==:==\nX : ")
    print("X  0   " if erros >= 1 else "X")

    linha2 = ""
    if erros == 2:
        linha2 = " | "
    elif erros == 3:
        linha2 = " \| "
    elif erros >= 4:
        linha2 = " \|/ "

    print("X%s" % linha2)

    linha3 = ""
    if erros == 5:
        linha3 += " /  "
    elif erros >= 6:
        linha3 += " / \ "
    print("X%s" % linha3)
    print(60 * "=")

    if erros == 6:
        print("Enforcado!")
        print("Palavra secreta: %s" % palavra)
        break
