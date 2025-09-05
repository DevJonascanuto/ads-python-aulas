# for
numeros = [1,2,3,4,5]

for num in numeros:
    print(num)


# while

numero = int(input('digite um numero (ou 0 para sair): '))

while numero != 0 :
    if numero % 2 == 0:
        print ('o numero é par.')
    else:
        print (' o numero é impar.')
    numero = int(input('digite outro numero (ou 0 para sair) : '))

# controle de repetiçao: range, break e continue

for x in range (5) :  # repetição por quantidade\\ vai de 0 ate 4 pois ele sempre para abaixo do limite no caso o 5
    print(x)

for y in range (2,7): # limites inicial e superior \\ aqui ele começa no 2 e para no 6 pois 7 seria o limite, ele sempre para um abaixo
    print(y)

for z in range (1,11,2): # com incremento \\ aqui ele vai de 1 A 11 pulando de 2 em 2 numeros, e novamente ele para antes do limitador que seria o 11
    print (z)


# pare ou siga \\ brake ou continue

for numero in range (1,11):
    if numero % 2 == 0:
        print('o primeiro numero par encontrado é: ', numero)
        break  # condição de parada


for numero in range (1,11):
    if numero == 5: # ele vai pular o numero 5
        continue
    print(numero)


