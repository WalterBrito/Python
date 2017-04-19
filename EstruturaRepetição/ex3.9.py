# -*- coding: utf-8 -*-

# Altere o programa anterior para mostrar no final a soma dos números.

print("==============================================================")

soma = 0
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

if num1 < num2:
	while num1 < num2:
		num1 += 1
		soma = soma + num1
		if num1 < num2:
			print(num1)

elif num2 < num1:
	while num2 < num1:
		num2 += 1
		soma = soma + num2
		if num2 < num1:
			print(num2)
			
print("Soma dos numeros no intervalo = %d" % soma)


print("==============================================================")
