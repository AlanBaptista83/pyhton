# Sintaxe:
# print(objetos, argumentos)

mensagem = 'Função Print()'
print(mensagem)
print('Aula de Python')

nome = 'Alan Baptista'
canal = 'Treinamento Python'
print(canal, '-', nome)

nome = (input('Digite seu nome: '))
# print('Olá, ' + nome + '!. Bem vindo ao curso de python!')
msg = 'Olá, ' + nome + '! Bem vindo ao curso de Python!'
print (msg)
print('Outro texto')

print('Imprime a mensagem e muda de linha')
print('Imprime a mensagem e permanece na linha. ', end='') # sem quebra de linha no print
print('Continuo na mesma linha.')

idade = 30
msg_formatada = 'O nome dela é {0} e ela tem {1} anos'.format(nome, idade)
print(msg_formatada)
print(f'O nome dela é \t {nome}\t  \n e ela tem {idade} anos.') # \n Força a quebra de linha 
# \t Gera uma tabulação 
# \\ Aparece uma barra invertida na tela

a = 10
b = 3
print(f'A média de {a} com {b} é igual a \'{a/b:.2f}\'') # \ é para indicar um caracter de escape = não será interpretado pelo python e aparece na tela as aspas