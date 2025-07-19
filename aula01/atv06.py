
raio = float(input('Digite o valor do raio: '))
altura = float(input('Digite o valor da altura: '))

pi = 3.14

area_lateral = 2 * pi * raio * altura
area_base = pi * (raio ** 2)
area_cilindro = area_base + area_lateral

qnt_litros = area_cilindro / 3
qnt_latas = qnt_litros / 5
valor = qnt_latas * 50


print(f"A área do cilindro é de {area_cilindro:.2f}, e você precisará de {qnt_latas:.2f} para pintar o cilindro. Tendo um valor final de R${valor:.2f}")


raio = float(input('Digite o valor do raio: '))
altura = float(input('Digite o valor da altura: '))

pi = 3.14

area_lateral = 2 * pi * raio * altura
area_base = pi * (raio ** 2)
area_cilindro = area_base + area_lateral

qnt_litros = area_cilindro / 3
qnt_latas = qnt_litros / 5
valor = qnt_latas * 50


print(f"A área do cilindro é de {area_cilindro:.2f}, e você precisará de {qnt_latas:.2f} para pintar o cilindro. Tendo um valor final de R${valor:.2f}")

