valor_compra = float(input('Digite o valor da compra: '))
pagamento = input('Digite a forma de pagamento: ').lower() #.upper()

if valor_compra > 250.0 and pagamento == 'vista':
    print(f'O valor final da compra é: {valor_compra*(1-0.16):.2f}')
else:
    print(f'O valor de compra é {valor_compra:.2f}')