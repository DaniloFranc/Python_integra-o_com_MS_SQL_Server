import pyodbc
import random
from faker import Faker


def retornar_conexao():
    server = 'localhost\\SQLEXPRESS'
    database = 'Novo_teste_python'
    username = 'DESKTOP-FUTO7UN\\Danil'
    password = ''
    string_conexao = f"Driver={{SQL Server Native Client 11.0}};Server={server};Database={database};UID={username};PWD={password};Trusted_Connection=yes;"
    conexao = pyodbc.connect(string_conexao)
    return conexao.cursor()




F = Faker()
email_aleatorio = []
n = []
dominios = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com"]
c = retornar_conexao()

try:
    c.execute("""Create table minha_tabela (
    id INT primary key,
    name VARCHAR(255),
    age INT,
    email VARCHAR(255))
    ;""")
    print("Tabela criada com sucesso!")
    c.commit()

except pyodbc.Error as ex:
    print("Erro ao criar a tabela:", ex)



try:

    for i in range(0,10):

        no = F.name()
        nome = F.name().replace(" ", "")
        n.append(nome)
        nome_aleatorio = random.choice(n)
        dominio_aleatorio = random.choice(dominios)
        r = random.randint(0,30)

        c.execute(f"INSERT INTO Persons (id, name, age, email) VALUES ({i},'{no}',{r},'{nome_aleatorio}@{dominio_aleatorio}');")

        c.commit()

except pyodbc as ex:

    print("Erro ao criar a tabela:", ex)




