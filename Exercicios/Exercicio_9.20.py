# -*- coding: utf-8 -*-

"""
Ao ler ou gravar uma nova lista, verifique se a agenda atual já
foi gravada. Você pode usar uma variavel para controlar quando
a lista foi alterada (novo, altera, apaga) e reinicializar esse 
valor quando ela for lida ou gravada. 
"""


print("=" * 60)

agenda = []

# Variavel para marcar uma alteração na agenda
alterada = False

def pede_nome():
     return(input("Nome: "))

def pede_telefone():
     return(input("Telefone: "))

def mostra_dados(nome, telefone):
     print("Nome: %s Telefone: %s" % (nome, telefone))

def pede_nome_arquivo():
     return(input("Nome do arquivo: "))

def pesquisa(nome):
     mnome = nome.lower()
     for p, e in enumerate(agenda):
         if e[0].lower() == mnome:
               return p
     return None

def novo():
     global agenda
     nome = pede_nome()
     telefone = pede_telefone()
     agenda.append([nome, telefone])
     alterada = True

def confirma(operação):
    while True:
        opção = input("Confirma %s (S/N)? " % operação).upper()
        if opção in "SN":
            return opção 
        else:
            print("Resposta inválida. Escolha S ou N")    

def apaga():
     global agenda
     nome = pede_nome()
     p = pesquisa(nome)
     if p != None:
        if confirma("exclusão") == "S":
            del agenda[p]
            alterada = True
     else:
         print("Nome não encontrado.")

def altera():
     p = pesquisa(pede_nome())
     if p != None:
         nome = agenda[p][0]
         telefone = agenda[p][1]
         print("Encontrado:")
         mostra_dados(nome, telefone)
         nome = pede_nome()
         telefone = pede_telefone()
         if confirma("alteração") == "S":
             agenda[p] = [nome, telefone]
             alterada = True
     else:
         print("Nome não encontrado.")

def lista():
     print("\nAgenda\n\n------")
     for posição, e in enumerate(agenda):
        print("Posição: %d " % posição, end="")
        mostra_dados(e[0], e[1])
     print("------\n")

def lê():
     global agenda
     nome_arquivo = pede_nome_arquivo()
     arquivo = open(nome_arquivo, "r", encoding = "utf-8")
     agenda = []
     for l in arquivo.readlines():
         nome, telefone = l.strip().split("#")
         agenda.append([nome, telefone])
     arquivo.close()
     alterada = False

def ordena():
    global alterada
    fim = len(agenda)
    while fim > 1:
        i = 0
        trocou = False 
        while i < (fim -1):
            if agenda[i] > agenda[i + 1]:
                temp = agenda[i + 1]
                agenda[i + 1] = agenda[i]
                agenda[i] = temp 
                trocou = True 
            i += 1
        if not trocou:
            break
        alterada = True        
            

def grava():
    global alterada
    if not alterada:
        print("Você não alterou a lista. deseja gravá-la mesmo assim?")
        if confirma("Gravação") == "N":
            return
    print("Gravar\n-----")       
    nome_arquivo = pede_nome_arquivo()
    arquivo = open(nome_arquivo, "w", encoding = "utf-8")
    for e in agenda:
        arquivo.write("%s#%s\n" % (e[0], e[1]))
    arquivo.close()
    alterada = False

def valida_faixa_inteiro(pergunta, inicio, fim):
     while True:
         try:
               valor = int(input(pergunta))
               if inicio <= valor <= fim:
                   return(valor)
         except ValueError:
               print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))

def menu():
     print("""
   1 - Novo
   2 - Altera
   3 - Apaga
   4 - Lista
   5 - Grava
   6 - Lê
   7 - Ordena por nome

   0 - Sai
""")
     print("\nNomes na agenda: %d\n" % len(agenda))
     return valida_faixa_inteiro("Escolha uma opção: ",0,7)

while True:
     opção = menu()
     if opção == 0:
         break
     elif opção == 1:
         novo()
     elif opção == 2:
         altera()
     elif opção == 3:
         apaga()
     elif opção == 4:
         lista()
     elif opção == 5:
         grava()
     elif opção == 6:
         lê()
     elif opção == 7:
         ordena()    


print("=" * 60)