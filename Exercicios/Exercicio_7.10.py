# -*- coding: utf-8 -*-

"""
Escreva um jogo da velha para dois jogadores. O jogo deve
perguntar onde você jogar e alternar entre os jogadores. A
cada jogada, verifique se a posição está livre. Verifique
também quando um jogador venceu a partida. Um jogo da velha
pode ser visto como uma lista de 3 elementos, onde cada
elemento é outra lista, também com três elementos.

Exemplo do jogo:

  X | 0 |
 ---+---+---
    | X | X
 ---+---+---
    |   | 0


Onde cada posição pode ser vista como um número. Confira abaixo
um exemplo das posições mapeadas para a mesma posição de seu
teclado numérico.


  7 | 8 | 9
 ---+---+---
  4 | 5 | 6
 ---+---+---
  1 | 2 | 3

"""


# O Tabuleiro
velha = """       Posições
   |   |        7 | 8 | 9
 --+---+---    ---+---+---
   |   |        4 | 5 | 6
 ---+---+---   ---+---+---
   |   |        1 | 2 | 3
"""

"""
Uma lista de posições (linhas e colunas) para cada posição válida
do jogo.
Um elemento extra foi adicionado para facilitar a manipulação dos
indices e para que estes tenham o mesmo valor da posição.

 7 | 8 | 9
 ---+---+---
 4 | 5 | 6
 ---+---+---
 1 | 2 | 3
"""

posições = [
    None,   # Elemento adicionado para facilitar indices
    (5, 1),  # 1
    (5, 5),  # 2
    (5, 9),  # 3
    (3, 1),  # 4
    (3, 5),  # 5
    (3, 9),  # 6
    (1, 1),  # 7
    (1, 5),  # 8
    (1, 9),  # 9
]

"""
Posições que levam ao ganho do jogo.
Jogas fazendo uma linha, uma coluna ou as diagonais ganham.
Os números representam as posições ganhadoras
"""

ganho = [
    [1, 2, 3],  # Linhas
    [4, 5, 6],
    [7, 8, 9],
    [7, 4, 1],  # Colunas
    [8, 5, 2],
    [9, 6, 3],
    [7, 5, 3],  # Diagonais
    [1, 5, 9]
]

"""
Controi o tabuleiro a partir das strings, gerando uma lista
de listas que pode ser modificada
"""
tabuleiro = []
for linha in velha.splitlines():
    tabuleiro.append(list(linha))

jogador = "X"   # Começa jogando com X
jogando = True
jogadas = 0    # Contador de jogadas - usadas para saber se velhou

while True:
    for t in tabuleiro:   # Imprime o tabuleiro
        print("".join(t))
    if not jogando:   # Termina após imprimir o últmo tabuleiro
        break
    if jogadas == 9:  # Se 9 jogadas, todas as posições já foram preenchidas
        print("Deu velha! ninguém ganhou.")
        break

    jogada = int(input("Digite a posição a jogar 1-9 (jogado %s): " % jogador))
    if jogada < 1 or jogada > 9:
        print("Posição inválida")
        continue

    # Verifica se a posição está livre
    if tabuleiro[posições[jogada][0]][posições[jogada][1]] != " ":
        print("Posição ocupada.")
        continue

    # Marca a jogada para o jogador
    tabuleiro[posições[jogada][0]][posições[jogada][1]] = jogador

    # Verifica se ganhou
    for p in ganho:
        for x in p:
            if tabuleiro[posições[x][0]][posições[x][1]] != jogador:
                break
        else:  # Se o for terminar sem o break, todas as posições de p pertecem ao mesmo jogador
            print("O jogador %s ganhou (%s): " % (jogador, p))
            jogando = False
            break
    jogador = "X" if jogador == "O" else "O"  # Alterna jogador
    jogadas += 1  # Contador de jogadas


"""
Sobre a conversão de coordenadas:
tabuleiro[posições[x][0]][posições[x][1]]

Como tabuleiro é uma lista de listas, podemos acessar cada caracter
especificando uma linha e uma coluna. Para obter a linha e a coluna, com base
na posição jogada, usamos a lista de posições que retorna uma tupla com 2 elementos:
linha e coluna. Sendo linha o elemento [0] e coluna o elemento [1].
O que estas linhas realizam é a conversão de uma posição de jogo (1-9)
em linhas e colunas do tabuleiro. Veja que neste exemplo usamos o tabuleiro como
memória de jogadas, além da exibição do estado atual do jogo.
"""
