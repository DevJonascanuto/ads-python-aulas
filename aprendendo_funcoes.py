
def soma (a,b):
    resultado = a + b
    return resultado

resultado_soma = soma (255 ,255)
print (resultado_soma)

# exercicios notas usando funçoes

notas = [9.5,10,8.5,6]  # aqui temos uma lista, no caso oque esta dentro de [] é uma lista, e essa lista se chama notas que é uma variavel
def calculo_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

media_final = calculo_media(notas)

if media_final >= 6:
    situacao = 'aprovado'
else:
    situacao = 'reprovado'

print (f'a media do aluno é {media_final} aluno {situacao}')
