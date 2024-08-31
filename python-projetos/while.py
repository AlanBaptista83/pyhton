num = 1
while (num <= 10):
    print(f'{num} ', end='')
    num += 1
print('Fim!')

nome = None # cria variável na memória vazia
while True:
    nome = input(f'Digite seu nome ou X para parar: ')
    if (nome == 'x') or (nome == 'X'):
        break
    print(f'Bem vindo, {nome}')
print('Volte sempre.')
    