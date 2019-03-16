# coding: utf-8

numbers = [1, 2, 3, 4, 5]
print(numbers)

words = ['salário', 'imposto']
print(words)

different_types = [1, 'salário']
print(different_types)

different_types = [[1, 2, 3], 'salário', 10]
print(different_types)

words = ['impostos', 'salários', 'altos', 'baixos']
print(words[0]) # impostos
print(words[-1]) # baixos
print(words[2:4]) # ['altos', 'baixos']

words[2] = 'Altos'
words[3] = 'Baixos'
print(words)

words[0:2] = ['Impostos', 'Salários']
print(words)

words = []

if words:
    print('Não sou executado')
else:
    print('Sempre sou executado')