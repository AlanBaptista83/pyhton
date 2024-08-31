# lista = [2, 6, 9, 4, 0 ,12 , 3, 7]
# for item in lista:
#     print(item, end=' ')


# print('\n')
# palavra = 'Baptista'
# for letra in palavra:
#     print(letra, end=' ')

# print('\n')
# for numero in range(1, 11): # pode colocar somente 1 número para repetir
#     print(numero, end=' ')

# print('\n')
# nome = input('Digite seu nome: ')
# for c in range (10):
#     print(f'{c+1} {nome}', end=' ')
# print('\n')

# range(valor_inicial, valor_final, incremento)
    
# for x in range(2, 20):
#     print(x, end=' ')
# print('\n')

# for x in range(2, 21, 2):
#     print(x, end=' ')
# print('\n')

# for x in range(20, 1, -2):
#     print(x, end=' ')
# print('\n')

pedras = ('rubi', 'esmeralda', 'quartzo', 'safira', 'diamante', 'turmalina')
for pedra in pedras:
    if (pedra == 'quartzo'):
        continue # encerra a iteração atual do laço e passa para a próxima iteração
    print(pedra)