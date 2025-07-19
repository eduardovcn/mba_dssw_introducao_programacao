peso = input("Qual o seu peso? ")
altura = input("Qual a sua altura? ")

#Trocando a virgula por ponto. Para manter o padrão americano
peso = peso.replace(',', '.') 
altura = altura.replace(',', '.')

#Convertendo para float após a troca, para que não haja erro de tipo
peso = float(peso)
altura = float(altura)


imc = peso / (altura ** 2)

print(f"O seu IMC é {imc:.1f}")


