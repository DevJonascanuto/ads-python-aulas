nota1 = int(input('digite a nota do aluno em matematica '))
nota2 = int(input('digite a nota do aluno em portugues '))
nota3 = int(input('digite a nota do aluno em educação fisica '))
nota4 = int(input('digite a nota do aluno em ingles '))
media = (nota1 + nota2 + nota3 + nota4) / 4
# condição para aprovação do aluno

if media >= 6:
    situação = 'aprovado'
else:
    situação = 'reprovado'

print(f'a média do aluno é {media:.1f} - situação: {situação}')
