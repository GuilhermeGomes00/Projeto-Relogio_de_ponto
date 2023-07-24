# input(
# "Qual horario deseja marcar? \nEntrada \nI
# )

import datetime


def arm():
    while True:
        pergunta = input(
            "Qual horario deseja marcar? \nEntrada \nInicio do almoço \nSaida do almoço \nSaida \nNenhum \n>"
        )
        pergunta = pergunta.lower()  # Convertendo para letras minúsculas
        if pergunta == "entrada":
            nome = input("Qual seu nome? ")
            entrada = datetime.datetime.now()  # entrada.strftime("%H:%M:%S")
            
            break
        elif pergunta == "Inicio de almoço":
            


arm()
