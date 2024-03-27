import random
import sys

# Verificar si se proporciona el número de valores como argumento
if len(sys.argv) != 3 or sys.argv[1] != "-n":
    print("Uso: python programa.py -n <num_valores>")
    sys.exit(1)

# Obtener el número de valores de los argumentos de la línea de comandos
num_valores = int(sys.argv[2])

# Generar los valores aleatorios entre 0 y 1 y almacenarlos en una lista
valores = [random.randint(0, 37) for _ in range(num_valores)]

# Calcular la frecuencia absoluta de cada valor
frecuencia_absoluta = {i: valores.count(i) for i in range(0,37)}



# Calcular la frecuencia relativa de cada valor
frecuencia_relativa  = {i: frecuencia_absoluta[i] / num_valores for i in range(0,37)}

# Imprimir los resultados
print("Valores generados:", valores)
for i in range(0,37):
    print(f"Frecuencia absoluta de {i}:", frecuencia_absoluta[i])
    print(f"Frecuencia relativa de {i}:", frecuencia_relativa[i])

