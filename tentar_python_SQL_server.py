import cursor as cursor
import pyodbc

def retornar_conexao_sql():

    server = 'localhost\SQLEXPRESS'
    database = 'Novo_teste_python'
    username = 'DESKTOP-FUTO7UN\Danil'
    string_conexao = f"Driver={{SQL Server Native Client 11.0}};Server={server};Database={database};UID={username};Trusted_Connection=yes;"
    conexao = pyodbc.connect(string_conexao)
    return conexao.cursor()



c = retornar_conexao_sql()

c.execute("SELECT * FROM usuarios")
rows = c.fetchall()
for row in rows:
    print(row)