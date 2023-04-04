import pyodbc

# configurações de conexão
server = 'localhost\\SQLEXPRESS'
database = 'Novo_teste_python'
username = 'DESKTOP-FUTO7UN\\Danil'
password = ''

# cria uma conexão com o banco de dados
conn = pyodbc.connect(f"Driver={{SQL Server Native Client 11.0}};Server={server};Database={database};UID={username};PWD={password};Trusted_Connection=yes;")

# define o nome da tabela a ser excluída
tabela = 'minha_tabela'

# cria um cursor para executar a consulta SQL
cursor = conn.cursor()

# executa a consulta SQL para excluir a tabela
cursor.execute(f"DROP TABLE {tabela}")

# confirma as alterações no banco de dados
conn.commit()

# fecha a conexão com o banco de dados
conn.close()

print(f"A tabela {tabela} foi excluída com sucesso.")

print()