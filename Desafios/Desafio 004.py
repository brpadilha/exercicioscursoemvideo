algo = input('\033[;33mDigite algo:\033[m ')
# print('O tipo primitivo desse valor é ',type(algo))
# print ('Só tem espaços? ',algo.isspace())
# print ('É um número? ', algo.isnumeric())
# print ('É um alfabeto? ',algo.isalpha())
# print('É um alfanumérico: ',algo.isalnum())
# print ('Está em maiúscula? ',algo.isupper())
# print ('Está em minúsculo? ',algo.islower())
# print ('Está capitalizada ?', algo.istitle())

print('O tipo primitivo desse valor é \033[;32m{}\033[m'.format(type(algo)))
print('Só tem espaços? \033[;32m{}\033[m'.format(algo.isspace()))
print('É um número ? \033[;32m{}\033[m'.format(algo.isnumeric()))
print('É um alfabeto? \033[;32m{}\033[m'.format(algo.isalpha()))
print('É um alfanumérico? \033[;32m{}\033[m'.format(algo.isalnum()))
print('É em maiúscula? \033[;32m{}\033[;m'.format(algo.isupper()))
print('É em minúsculo? \033[;32m{}\033[;m'.format(algo.islower()))
print('Esta capitalizada? \033[;32m{}\033[;m '.format(algo.istitle()))
