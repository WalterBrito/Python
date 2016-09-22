# -*- coding: utf-8 -*-

"""
Escreva um programa que pergunte o valor inicial de uma
divida e o juro mensal. Pergunte também o valor mensal que
será pago. Imprima o número de meses que a divida seja paga,
o total pago e o total de juros pago.
"""

print(60 * "=")

divida = float(input("Digite o valor da divida: "))
juro = float(input("Digite o valor do juro: "))
valMensal = float(input("Digite o valor mensal a ser pago: "))

mês = 1
if (divida * (juro / 100) > valMensal):
    print("Divida não acabará!")
    print("Juros são superiores ao pagamento mensal.")
else:
    saldo = divida
    jurosPago = 0

    while saldo > valMensal:
        taxa = saldo * juro / 100
        saldo = saldo + taxa - valMensal
        jurosPago = jurosPago + taxa
        print("Saldo do mês %d é de R$ %.2f" % (mês, saldo))
        mês = mês + 1
    print("Para pagar uma divida de R$ %.2f, a %.2f %% juros" % (divida, taxa))
    print("Você precisará de %d meses, pagando um total de R$ %.2f de juros." %
          (mês - 1, jurosPago))
    print("No último mês, você teria um saldo residual de R$ %.2f a pagar." % (saldo))

print(60 * "=")
