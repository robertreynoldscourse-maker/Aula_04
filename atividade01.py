valor_compra = float(input('Digite o valor da compra: '))

if valor_compra > 250.0:
    print(f'O valor final da compra é: {valor_compra*(1-0.16)}')
else:
    print(f'O valor de compra é {valor_compra}')