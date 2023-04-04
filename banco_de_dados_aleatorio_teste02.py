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
P = ''
s = 0
dominios = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com"]
profissões = ["gerente","encarregado","vendedor","serviços gerais"]

c = retornar_conexao()

try:
    c.execute("""Create table Persons (
    id INT primary key,
    name VARCHAR(255),
    age INT,
    email VARCHAR(255),
    salário FLOAT,
    função VARCHAR(255))
    ;""")
    print("Tabela criada com sucesso!")
    c.commit()

except pyodbc.Error as ex:
    print("Erro ao criar a tabela:", ex)



try:

    for i in range(0,1000001):

        no = F.name()
        nome = F.name().replace(" ", "")
        n.append(nome)
        nome_aleatorio = random.choice(n)
        P = random.choice(profissões)
        dominio_aleatorio = random.choice(dominios)
        r = random.randint(18,65)
        s = random.randint(1500,3000)





        c.execute(f"INSERT INTO Persons (id, name, age, email, salário, função) VALUES ({i},'{no}',{r},'{nome_aleatorio}@{dominio_aleatorio}',{s},'{P}');")

        c.commit()

except pyodbc as ex:

    print("Erro ao criar a tabela:", ex)


