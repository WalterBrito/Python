import salaryControl

# Cria arquivos com os gastos em um arquivo txt
arquivo = 'gastos.txt'

# Função gastos
def gastosMensal():
    # Escreve os gastos no arquivo txt criado.
    arquivo_txt = open(arquivo, 'w')
    for key in contasPagar:
        arquivo_txt.write("%s: %f\n" % (key, contasPagar[key]))

gastosMensal()