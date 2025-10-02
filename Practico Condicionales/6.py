import random
import statistics

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = statistics.mode(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
media = statistics.mean(numeros_aleatorios)

if media > mediana:
    sesgo = "Sesgo positivo"
elif media < mediana:
    sesgo = "Sesgo negativo"
else:
    sesgo = "No hay sesgo"


print("Lista de números aleatorios:", numeros_aleatorios)
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media:.2f}")
print(sesgo)