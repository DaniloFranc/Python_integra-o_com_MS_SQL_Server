import pyodbc
import random
import string
from faker import Faker

def retornar_conexao():
    server = 'localhost\\SQLEXPRESS'
    database = 'Novo_teste_python'
    username = 'DESKTOP-FUTO7UN\\Danil'
    password = ''
    string_conexao = f"Driver={{SQL Server Native Client 11.0}};Server={server};Database={database};UID={username};PWD={password};Trusted_Connection=yes;"
    conexao = pyodbc.connect(string_conexao)
    return conexao.cursor()



c = retornar_conexao()

fake = Faker()

try:

    c.execute("""CREATE TABLE clientes (
        id INT PRIMARY KEY,
        nome VARCHAR(255),
        idade INT
    );""")

    print("Tabela criada com sucesso!")
    c.commit()

except pyodbc.Error as ex:
    print("Erro as criar a tabela:", ex)

for i in range(1,21):

    nome_aleatorio = fake.name()

    numero_aleatorio = random.randint(0, 30)


    try:
        c.execute(f"INSERT INTO clientes (id, nome, idade) VALUES ({i}, '{nome_aleatorio}', '{numero_aleatorio}');")

        c.commit()

        print("Dados inseridos com sucesso!")

    except pyodbc.Error as ex:
        print("Erro as criar a tabela:", ex)