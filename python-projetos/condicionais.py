# Simples, Composto ou Encadeado

n1 = n2 = media = 0.0
n1 = float(input('Digite sua 1ª nota: '))
n2 = float(input('Digite sua 2ª nota: '))
media = (n1 + n2) / 2
if (media >= 7):
    print(f'Aluno Aprovado. Média: {media}')
elif (media >= 5):
        print(f'Você está de recuperação. Média {media}')
        recupera = float(input('Digite nota da recuperação: '))
        if (recupera >= 7):
             print(f'Aluno aprovado. Nota recuperação foi {recupera}')
        else:
            print(f'Aluno reprovado. Média {media} na recuperação')
else:
    print(f'Aluno reprovado. Média {media}')
