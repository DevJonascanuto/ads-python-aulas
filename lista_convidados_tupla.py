convidados = ('joao','gabriel','alice','rangel','isabel')
confirmado = ['joao','alice']
nao_confirmados = [convidado for convidado in convidados if convidado not in confirmado]
print ('convidados que ainda nao confirmaram')
for pessoa in nao_confirmados:
    print(pessoa)