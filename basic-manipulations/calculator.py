# coding: utf-8

tax = 0.27
salary = 5000

print('Salário real: {}'.format(salary - salary * tax)) # Salário real: 3650.0
print('Imposto: {}'.format(salary * tax)) # Salário real: 1350.00

salary = 3000

print('Valor real: {0}'.format(salary - salary * tax)) # Valor real: 2190.0