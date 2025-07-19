
peso = float(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura em metros? "))

peso = peso.replace(',', '.') 
altura = altura.replace(',', '.')

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Peso normal")
elif imc <= 29.9:
    print("Sobrepeso")
elif imc <= 34.9:
    print("Obesidade grau 1")
elif imc <= 39.9:
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3")






