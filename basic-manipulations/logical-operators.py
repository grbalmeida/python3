tax = float(input('Imposto: '))

if tax < 10.:
    print('Baixo')
elif tax >= 10. and tax <= 27.:
    print('Médio')
elif tax > 27. and tax < 100:
    print('Alto')
else:
    print('Imposto inválido')