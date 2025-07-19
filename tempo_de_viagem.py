
distancia = float(input("Qual a distância da sua viagem em km? "))
vel_media = float(input("Qual a velocidade média? "))

tempo_total = distancia / vel_media

horas = int(tempo_total) #descarta a fração
minutos = (tempo_total - horas) * 60

print(f"A viagem terá uma duração de {horas} horas e {minutos} minutos")