
peso = float(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura em metros? "))

peso = peso.replace(',', '.') 
altura = altura.replace(',', '.')

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
elif imc < 35:
    print("Obesidade grau 1")
elif imc < 40:
    print("Obesidade grau 2")
elif imc >= 40:
    print("Obesidade grau 3")






