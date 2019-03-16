# coding: utf-8

salary = int(input('Salário? '))
tax = input('Imposto em % (ex: 27.5)? ')

if not tax:
    tax = 27.5
else:
    tax = float(tax)

print('Valor real: {0}'.format(salary - salary * tax * 0.01))

if tax < 10:
    print('Médio')
elif tax < 27.5:
    print('Alto')
else:
    print('Muito alto')

tax = 0.3
print('Alto' if tax > 0.27 else 'Baixo') # Alto

tax = 0.10
print('Alto' if tax > 0.27 else 'Baixo') # Baixo

tax_amount = 'Alto' if tax > 0.27 else 'Médio'
print(tax_amount) # Médio