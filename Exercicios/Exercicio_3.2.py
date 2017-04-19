# -*- coding: utf-8 -*-

"""
Escreva uma expressão que será utilizada  para decidir se 
um aluno foi ou não aprovado. Para ser aprovado, todas as médias do
aluno devem ser maiores que 7. Considere que o aluno cursa três matérias,
e que a nota de cada uma está armazaneda nas seguintes variavéis:
matéria1, matéria2 e matéria3.
"""

print(60 * "=")
matéria1 = 8
matéria2 = 9
matéria3 = 6.5

media = (matéria1 + matéria2 + matéria3 / 3)

if media >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")
print(60 * "=")
