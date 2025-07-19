# ESTRUTURAS DE CONTROLE

# ESTRUTURA SEQUENCIAL

""" 
- Desvio Condicional
   - Estrutura de Seleção Simples if
   - Estrutura de Seleção Encadeada  and
   - Estrutura de Seleção Composta else
   
   """
print("Iniciando o Programa")

media = 6.0

if media >= 7.0:
    print("Aprovado")
else:
    print("Reprovado")

print("Finalizando o Programa\n")

print("--------------------------------------------------------------------------")




idade = int(input("Qual a sua idade? "))
ingresso = input("Ingresso VIP ou PISTA? ").upper() #converter tudo em caixa alta


if idade >= 18:
    print("Pode entrar na festa!\n")
else:
    print("Não pode entrar na festa!\n")

if idade >= 18 and ingresso == "VIP":
    print("Pode entrar na festa!\n")
else:
    print("Não pode entrar na festa!\n")



print("--------------------------------------------------------------------------")



"""ESTRUTURA DE SELEÇÃO ANINHADA"""
nota = 9
if nota == 7:
    if nota >= 7 and nota <= 8:
        print("Bom Trabalho!")
    elif nota >= 9 and nota <= 10:
        print("Excelente Trabalho!")
    else: 
        print("Trabalho perfeito!")





    

