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
# Logic

nome_funcionario = "Marco"

entrada = datetime.datetime.now()  # entrada.strftime("%H:%M:%S")
entrada = entrada.strftime("%Y/%m/%d")

command = (
    f"INSERT INTO marca_ponto (nome, dia) VALUES ('{nome_funcionario}', '{entrada}');"
)

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
