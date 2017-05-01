# Cria arquivos com os gastos em um arquivo txt
arquivo = 'gastos.txt'

# Função para controlar salário
def controleSalario():
    # Dicionário vazio par armazenar as conats com seus valores
    contasPagar = {}

    # Recebe o valor do salário do usuário
    salario = float(input("Digite o valor do salário (ex: 1980.58): "))
    print('\n')

    total = 0
    # Pede informações do usuário até que digite s (Sair)
    while True:
        # User enter the expenses and salary
        gastos = input("Digite o nome do gasto á pagar (ex: Conta de luz): ").capitalize()
        valorConta = float(input("Digite o valor do gasto á pagar (ex: 52.90): "))
        sair = input('Deseja continuar? (S-Sim ou N-Não): ').lower()
        print('\n')

        if True:
            contasPagar[gastos] = valorConta
            total += valorConta
        else:
            print('Opção Inválida!\n Tente novamente.')

        # Sai do programa quando usuário pressiona s
        if sair == 'n':
            break

    print('========== Seus Gastos ==========\n')
    for key, value in contasPagar.items():
        print("{}: R${}".format(key, value))
    print('Total: R$%d Reais' % total)
    print('Obrigado!\n')

    # Escreve os gastos no arquivo txt criado.
    arquivo_txt = open(arquivo, 'w')
    for key in contasPagar:
        arquivo_txt.write("%s: %f\n" % (key, contasPagar[key]))

controleSalario()








