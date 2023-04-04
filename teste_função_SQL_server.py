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

    c.execute("""CREATE TABLE Valores (
        X INT PRIMARY KEY,
        Y INT,
    );""")

    print("Tabela criada com sucesso!")
    c.commit()

except pyodbc.Error as ex:
    print("Erro as criar a tabela:", ex)



for i in range(-100,101):

    try:
        c.execute(f"INSERT INTO Valores (X, Y) VALUES ({i}, '{i**3 + i**2}');")

        c.commit()

        print("Dados inseridos com sucesso!")

    except pyodbc.Error as ex:
        print("Erro as criar a tabela:", ex)