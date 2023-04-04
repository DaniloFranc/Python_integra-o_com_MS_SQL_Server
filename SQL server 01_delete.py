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
    c.execute("""DROP TABLE Persons;""")
    print("Tabela deletada com sucesso!")
    c.commit()

except pyodbc.Error as ex:
    print("Erro ao criar tabela:", ex)