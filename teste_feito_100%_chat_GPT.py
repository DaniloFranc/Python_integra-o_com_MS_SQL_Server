import pyodbc
import random
import string

# Defina as credenciais do SQL Server
server = 'localhost\\SQLEXPRESS'
database = 'Novo_teste_python'
username = 'DESKTOP-FUTO7UN\\Danil'
password = ''

# Estabeleça a conexão com o banco de dados
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

# Defina a lista de colunas da tabela
colunas = ['id', 'nome', 'idade', 'email']

# Defina o tipo de dados de cada coluna
tipos = ['INT', 'VARCHAR(50)', 'INT', 'VARCHAR(100)']

# Defina a consulta SQL para criar a tabela
query_criar_tabela = 'CREATE TABLE tabela_teste ('

for i in range(len(colunas)):
    query_criar_tabela += colunas[i] + ' ' + tipos[i] + ', '

query_criar_tabela = query_criar_tabela[:-2] + ')'

# Execute a consulta para criar a tabela
cursor = cnxn.cursor()
cursor.execute(query_criar_tabela)
cnxn.commit()

# Insira 300 linhas de dados aleatórios na tabela
for i in range(300):
    nome = ''.join(random.choices(string.ascii_uppercase, k=10))
    idade = random.randint(18, 65)
    email = nome.lower() + '@empresa.com'
    query_inserir_dados = f"INSERT INTO tabela_teste (nome, idade, email) VALUES ('{nome}', {idade}, '{email}')"
    cursor.execute(query_inserir_dados)
    cnxn.commit()

# Feche a conexão com o banco de dados
cnxn.close()