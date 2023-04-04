import pyodbc

def retornar_conexao_sql():
    server = 'localhost\\SQLEXPRESS'
    database = 'Novo_teste_python'
    username = 'DESKTOP-FUTO7UN\\Danil'
    password=' '
    string_conexao = f"Driver={{SQL Server Native Client 11.0}};Server={server};Database={database};UID={username};PWD={password};Trusted_Connection=yes;"
    conexao = pyodbc.connect(string_conexao)
    return conexao.cursor()



cursor = retornar_conexao_sql()

# Criar a tabela clientes
try:
    cursor.execute("""CREATE TABLE clientes (
        id INT PRIMARY KEY,
        nome VARCHAR(255),
        idade INT
    );""")
    print("Tabela criada com sucesso!")

except pyodbc.Error as ex:
    print("Erro ao criar tabela:", ex)

# Inserir dados na tabela


try:
    cursor.execute("""INSERT INTO clientes (id, nome, idade) VALUES
        (1, 'João', 30),
        (2, 'Maria', 25),
        (3, 'José', 35);""")
    cursor.commit()

    print("Dados inseridos com sucesso!")
except pyodbc.Error as ex:
    print("Erro ao inserir dados:", ex)

# Fechar a conexão
cursor.close()