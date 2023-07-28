# Libs

import mysql.connector
import datetime

# --------------------------------------------
# connection

conexao = mysql.connector.connect(
    host="localhost", user="root", password="10203040Gu!s", database="horario"
)
cursor = conexao.cursor()  # Conexão realizada aqui
print('-------------------------------------')
print('Conectando-se ao servidor...')
print('-------------------------------------')

# --------------------------------------------------
# Logic

while True:
    print('-------------------------------------')
    nome_funcionario = input("Qual seu nome? ")
    print('-------------------------------------')
    nome_funcionario = nome_funcionario.lower()

    pergunta = input(
        f"Bom dia, {nome_funcionario}! Qual ponto deseja marcar? "
        + "\nEntrada \nInicio do almoço \nSaida do almoço \nSaida \nNenhum \n> "
    )
    print('-------------------------------------')
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
        print(
            f"Inicio do almoço atualizado com sucesso! Tenha um ótimo descanso, {nome_funcionario}."
        )
        break

    elif pergunta == "saida do almoço":
        saida_almoco = datetime.datetime.now()
        saida_almoco = saida_almoco.strftime("%H:%M:%S")

        atualizar_sql = (f"UPDATE marca_ponto SET SaidaAlmoco = '{saida_almoco}' WHERE nome = '{nome_funcionario}'")
        cursor.execute(atualizar_sql)
        conexao.commit()
        print(f"Inicio do almoço atualizado com sucesso! Espero que tenha tido uma ótima refeição {nome_funcionario}.")
        break

    elif pergunta == "saida":
        saida = datetime.datetime.now()
        saida = saida.strftime("%H:%M:%S")

        atualizar_sql = (f"UPDATE marca_ponto SET HoraSaida = '{saida}' WHERE nome = '{nome_funcionario}'")
        cursor.execute(atualizar_sql)
        conexao.commit()
        print(f"Saida atualizado com sucesso! Até mais, {nome_funcionario}!")
        break

    else:
        print('-------------------------------------')
        print('ops... Algum erro ocorreu, por favor, tente novamente')
        print('-------------------------------------')

