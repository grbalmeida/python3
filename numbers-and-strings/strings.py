# coding: utf-8

print("Copa 2014")
print('Copa do mundo 2014')
print('''2014 - Copa do mundo''')
print("copa 'padrão fifa'")
print('copa "padrão fifa"')

print('''\
Uso: consulta_base [OPCOES]
    -h                   Exibe saída de ajuda
    -U url)              Url do dataset
''')

print(("Copa" "2014")) # Copa2014

print('Em qual cidade o legado da Copa foi mais relevante '
      'para a população')

string = "maracana"

print(string[0]) # 'm'
print(string[1:4]) # 'ara'
print(string[2:]) # 'racana'
print(string[:3]) # 'mar'

print(len(string)) # 8

print('m' in 'maracana') # True
print('x' not in 'maracana') # True
print('m' + 'aracana') # 'maracana'
print('a' * 3) # 'aaa'

# my_string = 'livro python 3'
# my_string[13] = '2'
# 'str' object does not support item assignment

my_string = 'livro python 3'
my_string = my_string[0:13] + '2'
print(my_string) # livro python 2

my_string = 'livro python 3'
my_string = my_string.replace('3', '2')
print(my_string) # livro python 2