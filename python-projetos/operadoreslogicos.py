idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))

# resultado = (idade >=18) and (altura >= 1.70)
# if resultado == True:
#     msg = 'Sim'
# else:
#     msg = 'Não'
# print(f'Pode participar do evento? {msg}')

resultado = (idade < 18) or (idade >= 60)
if resultado == True:
    msg = 'Ganha desconto no ingresso'
else:
    msg = 'Não tem direito a desconto'
print(f'Pela sua idade... {msg}')
