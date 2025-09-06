# crie um programa que so permita o carro passar o cruzamento, caso o semaforo esteja verde.

semaforo = (input('digite se o sinal esta (verde, amarelo ou vermelho )')).lower ()
if semaforo == 'verde':
    print ('siga')

elif semaforo == 'amarelo':
    print ('atenção')
else:
    print ('pare')
