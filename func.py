import datetime
import mysql.connector
from func import perg

'''def logic()

    nome_funcionario = input('Qual seu nome?')
    nome_funcionario = nome_funcionario.lower()
    pergunta = input(f'Bom dia, {nome}! Qual ponto deseja marcar? ' + '\nEntrada \nInicio do almoço \nSaida do almoço \nSaida \nNenhum \n>')
    pergunta = pergunta.lower()

    while True:
        
        if pergunta == "Entrada":

            def resp():
                entrada = datetime.datetime.now()  # entrada.strftime("%H:%M:%S")

                command = f"INSERT INTO marca_ponto (nome, dia) VALUES ('{nome_funcionario}', '{entrada.%H:%M:%S}');"

        
        elif pergunta == "Nenhum":
            break

    def perg():
        while True:

            def resp1():
                pergunta = input(
                    "Qual horario deseja marcar? \nEntrada \nInicio do almoço \nSaida do almoço \nSaida \nNenhum \n>"
                )
                pergunta = pergunta.lower()

                if pergunta == "Entrada":
                    nome = input("Qual seu nome? ")
                    entrada = datetime.datetime.now()  # entrada.strftime("%H:%M:%S")
                    break

                elif pergunta == "Nenhum":



perg()'''




cursor = conexao.cursor()


nome_funcionario = ''


consulta_sql = "SELECT * FROM funcionarios WHERE Nome = %s"


cursor.execute(consulta_sql, (nome_funcionario,))


registro_encontrado = cursor.fetchone()

# Verifique se encontrou o registro
if registro_encontrado:
    # Recupere o ID do registro (caso a tabela tenha uma coluna ID)
    id_registro = registro_encontrado[0]

    # Atualize os outros campos que deseja modificar
    dia = '2023-07-26'
    hora_entrada = '09:00:00'
    inicio_almoco = '12:30:00'
    saida_almoco = '13:30:00'
    hora_saida = '18:00:00'

    # Consulta SQL para atualizar o registro com as novas informações
    atualizar_sql = "UPDATE funcionarios SET Dia = %s, HoraEntrada = %s, InicioAlmoco = %s, SaidaAlmoco = %s, HoraSaida = %s WHERE id = %s"

    # Executa a atualização com os valores como parâmetros
    cursor.execute(atualizar_sql, (dia, hora_entrada, inicio_almoco, saida_almoco, hora_saida, id_registro))

    # Confirme a alteração
    conexao.commit()

    print("Registro atualizado com sucesso!")
else:
    print("Registro não encontrado.")

# Feche o cursor e a conexão
cursor.close()
conexao.close()












































