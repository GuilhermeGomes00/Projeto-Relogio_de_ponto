# Libs

import mysql.connector
import datetime

# --------------------------------------------
# connection

conexao = mysql.connector.connect(
    host="localhost", user="root", password="10203040Gu!s", database="horario"
)
cursor = conexao.cursor()  # Conexão realizada aqui

# --------------------------------------------------
# Logicc


def arm():
    while True:
        pergunta = input(
            "Qual horario deseja marcar? \nEntrada \nInicio do almoço \nSaida do almoço \nSaida \n Nenhum \n>"
        )
        pergunta = pergunta.lower()
        if pergunta == "Entrada":
            nome = input("Qual seu nome? ")
            entrada = datetime.datetime.now()  # entrada.strftime("%H:%M:%S")
            break


# --------------------------------------------------
# Commands


# command = f"INSERT INTO Pessoas (nome) VALUES ('{}]');"
cursor.execute(command)
conexao.commit()


"""

    nome = input("Qual seu nome? ")
    dia = datetime.datetime.now() # dia.strftime("%Y/%m/%d")
    entrada = datetime.datetime.now() # entrada.strftime("%H:%M:%S")
    entrada_almoco = datetime.datetime.now() # .strftime("%H:%M:%S")
    saida_almoco = datetime.datetime.now() #.strftime("%H:%M:%S")
    saida = datetime.datetime.now() # .strftime("%H:%M:%S")

"""
