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

while True:
    nome_funcionario = input("Qual seu nome?")
    nome_funcionario = nome_funcionario.lower()

    pergunta = input(
        f"Bom dia, {nome_funcionario}! Qual ponto deseja marcar? "
        + "\nEntrada \nInicio do almoço \nSaida do almoço \nSaida \nNenhum \n>"
    )
    pergunta = pergunta.lower()

    if pergunta == "entrada":
        dia = datetime.datetime.now()
        dia = dia.strftime("%Y/%m/%d")
        entrada = datetime.datetime.now()
        entrada = entrada.strftime("%H:%M:%S")

        command = (f"INSERT INTO marca_ponto (nome, dia, HoraEntrada) VALUES ('{nome_funcionario}', '{dia}', '{entrada}');")
        cursor.execute(command)
        conexao.commit()
        print("Seu nome e hora de entrada foi marcado, tenha um ótimo dia!")
        break

    elif pergunta == "inicio do almoço":
        inicio_almoco = datetime.datetime.now()
        inicio_almoco = inicio_almoco.strftime("%H:%M:%S")

        atualizar_sql = (f"UPDATE marca_ponto SET InicioAlmoco = '{inicio_almoco}' Where nome = '{nome_funcionario}'")
        cursor.execute(atualizar_sql)
        conexao.commit()
        print("Inicio do almoço atualizado com sucesso! Tenha um ótimo descanso.")
        break

# --------------------------------------------------
# Commands

# cursor.execute(command)
# conexao.commit()


"""

    nome = input("Qual seu nome? ")
    dia = datetime.datetime.now() # dia.strftime("%Y/%m/%d")
    entrada = datetime.datetime.now() # entrada.strftime("%H:%M:%S")
    entrada_almoco = datetime.datetime.now() # .strftime("%H:%M:%S")
    saida_almoco = datetime.datetime.now() #.strftime("%H:%M:%S")
    saida = datetime.datetime.now() # .strftime("%H:%M:%S")

"""
