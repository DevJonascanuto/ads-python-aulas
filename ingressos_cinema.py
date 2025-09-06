print ('bem vindo a maquina de vendas automatica de ingressos de cinema')

idade = int(input('Por favor digite a sua idade '))
if idade < 12:
    print ('voçe ainda é uma criança, recomendamos o filme infantil')

elif 12 <= idade < 18:
    print ('voçe é menor de idade, recomendamos o filme adolecente')

else:
    print ('voçe é maior de idade recomendamos o filme emocionante') 
