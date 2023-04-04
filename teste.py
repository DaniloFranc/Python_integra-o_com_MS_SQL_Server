from faker import Faker

fake = Faker()

for i in range(10):

    nome_aleatorio = fake.name()
    print(nome_aleatorio)