import random
import string

caracteres = string.ascii_letters


sequencia_aleatoria = ''.join(random.choice(caracteres) for i in range(6))

print(sequencia_aleatoria)