import math

import pyodbc

def retornar_conexao():
    server = 'localhost\\SQLEXPRESS'
    database = 'Novo_teste_python'
    username = 'DESKTOP-FUTO7UN\\Danil'
    password = ''
    string_conexao = f"Driver={{SQL Server Native Client 11.0}};Server={server};Database={database};UID={username};PWD={password};Trusted_Connection=yes;"
    conexao = pyodbc.connect(string_conexao)
    return conexao.cursor()





c = retornar_conexao()

try:

    c.execute("""CREATE TABLE Cardiaca (
        X FLOAT PRIMARY KEY,
        Y FLOAT,
    );""")

    print("Tabela criada com sucesso!")
    c.commit()

except pyodbc.Error as ex:
    print("Erro as criar a tabela:", ex)



for i in range(0,179):



    try:

        c.execute(f"INSERT INTO Cardiaca (X, Y) VALUES ({round((3*math.cos(math.radians(i)) + 3*math.cos(math.radians(i))**2),6)},'{round((3*math.sin(math.radians(i)) + 3*math.cos(math.radians(i))*math.sin(math.radians(i))),6)}');")

        c.commit()

        print("Dados inseridos com sucesso!")

    except pyodbc.Error as ex:
        print("Erro as criar a tabela:", ex)