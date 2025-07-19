print('\nCálculo de Desconto\n')

valor = float(input('Qual o valor? '))
desconto = float(input('Quanto de desconto será aplicado? '))

valor_do_desconto = (desconto / 100) * valor
valor_final =  valor - valor_do_desconto

print(f'Você terá um desconto de: {valor_do_desconto:.2f} e seu valor final ficará em: {valor_final:.2f}')