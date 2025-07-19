temp = int(input("Qual a temperatura você deseja converter? "))

medida = input("Qual a unidade de medida C/F? ").upper()

if medida == "C":
    temp_f = (temp * (9/5)) + 32
    print(f"A temperatura em Fahrenheit é: {temp_f:.2f}")
elif medida == "F":
    temp_c = (temp - 32) * (5/9)
    print(f"A temperatura em Celsius é: {temp_c:.2f}")
    
else:
    print("Unidade de medida inválida")