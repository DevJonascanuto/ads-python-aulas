filmes = ["Matrix", "Vingadores", "Titanic", "Avatar", "Interestelar"]

for filme in filmes:
    nota = input (f'qual nota de 1 a 5 para o {filme} ou SAIR para encerrar  ')
    notas = nota
    if nota == 'sair':
        print ('programa encerrado')
        break

print (f'essas foram as suas notas para o filme {notas}')
