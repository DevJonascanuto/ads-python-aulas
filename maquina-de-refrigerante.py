# desafio da semana, criar sistema de maquina de refrigerante, que calcula troco, e entrega produto somente com o pagamento correto.

produtos = [
    {'nome': 'coca-cola', 'preco':5.00, 'estoque':5},
    {'nome': 'batata-frita', 'preco':7.00, 'estoque': 6},
    {'nome': 'chocolate', 'preco': 10.50, 'estoque': 10},

]

print ('maquina de snacks')
for i, produto in enumerate (produtos):
    print(f'{i+1}). {produto['nome']} - R$ {produto['preco']} (estoque : {produto['estoque']}')

opcao = int(input('escolha o produto (numero):')) -1
produto = produtos [opcao]

# inserir dinheiro

valor_inserido = float(input('insira o valor em R$ :'))

if produto ['estoque'] <= 0:
    print ('PRODUTO ESGOTADO')

elif valor_inserido < produto ['preco']:
    print ('SALDO INSUFITIENTE!')

else:
    troco = valor_inserido - produto['preco']
    produto ['estoque'] -= 1
    print (f'voce recebeu : {produto['nome']}')
    if troco > 0:
        print (f'seu troco é : R$ {troco :.2f}')

