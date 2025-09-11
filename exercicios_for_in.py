# 1- Imprima os números de 1 a 10.

for x in range (11):
    print(x)


# 2- Imprima apenas os números pares de 1 a 20.

for par in range(21):
    if par % 2 == 0:
       print ('os numeros pares são :' , par)

# 3 - Peça uma palavra ao usuário e imprima cada letra separada.
palavra = input('digite uma palavra que vou mostrar separadamente cada letra ')
for letras, indice in enumerate (palavra): # enumerate vai numerar , for letras percorre as letras da palavra digitada enquanto enumerate conta
    print (letras,indice)



# 4 - Crie uma lista com nomes de 5 amigos e imprima cada um deles.
amigos = ['corlaite','ladeira','lacerda','rafael','windows']
for lista in amigos:
    print (lista)

# 5 - Peça uma frase ao usuário e conte quantas vogais (a, e, i, o, u) existem nela.
frase = input('digite uma frase que vou contar quantas vogais tem')
vogais = 'aeiou'
contador = 0 
for letra in frase:
    if letra in vogais:
        contador +=1

print('o numero de vogais é ', contador)




# 6 - Dada a lista numeros = [3, 7, 10, 15, 22], crie uma nova lista com o quadrado de cada número.

numeros = [3,7,10,15,22]
quadrados = [n ** 2 for n in numeros]
print(f'o numeo quadrado de 3,7,10,15,22 é {quadrados}')


# 7 - Use enumerate para imprimir os nomes de uma lista numerados (exemplo: 1 - João).

# 8 - Some todos os números de 1 a 100 usando for.