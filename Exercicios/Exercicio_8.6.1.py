# -*- coding: utf-8 -*-

# Exemplo varivael global e local

print(60 * "=")


a = 5


def mudaImprime():
    a = 7
    print("A dentro da função: %d" % a)
print("a antes de mudar: %d" % a)

mudaImprime()
print("a depois de mudar: %d" % a)


# Valor de agora será alterado
# a = 5

# def mudaImprime():
# 	global a
# 	a = 7
# 	print("A dentro da função: %d" % a)
# print("a antes de mudar: %d" % a)

# mudaImprime()
# print("a depois de mudar: %d" % a)


print(60 * "=")
