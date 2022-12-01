#4. Digite alguma palavra e utilize algumas funções do objeto

value = input('Digite algo: ')

print(type(value))
print('Ele é alfanumérico? ', value.isalnum())
print('Ele é alfa? ', value.isalpha())
print('Ele é decimal? ', value.isdecimal())
print('Ele é numérico? ', value.isnumeric())
print('Ele pode ser impresso? ', value.isprintable())
print('Ele só tem espaços? ', value.isspace())
print('Está capitalizada? ', value.istitle())