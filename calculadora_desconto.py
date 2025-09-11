valor_produto = float(input('digite o valor do produto : '))
percentual_desconto = float(input('digite o percentual de desconto :'))

if percentual_desconto < 0 or percentual_desconto > 80:
    print('erro o desconto deve estar entre 0% a 80% ')
else:
    desconto = valor_produto * (percentual_desconto / 100)

valor_final = valor_produto - desconto

print(f'o valor com desconto é R$: {valor_final:.2f}')
