from faker import Faker
import random

F = Faker()
email_aleatorio = []
n = []
dominios = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com"]

for i in range(0,10):

    nome = F.name().replace(" ","")
    n.append(nome)
    no = F.name()
    print(no)


for j in range(0,10):

    nome_aleatorio = random.choice(n)
    dominio_aleatorio = random.choice(dominios)

    #email_aleatorio.append(f"{nome_aleatorio}@{dominio_aleatorio}")

    print(f"{nome_aleatorio}@{dominio_aleatorio}")

print(random.randint(0,30))




