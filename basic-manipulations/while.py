# coding: utf-8

salary = int(input('Salário? '))
tax = 27.

while tax > 0.:
    tax = input('Imposto ou (0) para sair: ')
    if not tax:
        tax = 27.
    else:
        tax = float(tax)
    print('Valor real: {0}'.format(salary - salary * tax * 0.01))