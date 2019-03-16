# coding: utf-8

salary = int(input('Salário? '))
tax = float(input('Imposto em % (ex: 27.5)? '))
print('Valor real: {0}'.format(salary - salary * tax * 0.01))