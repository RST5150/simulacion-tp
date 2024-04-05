import random
import sys
import matplotlib.pyplot as plt


def are_arguments_ok():
    # Verificar si los argumentos enviados son correctos
    if len(sys.argv) != 7 or sys.argv[1] != "-c" or sys.argv[3] !='-n' or sys.argv[5]!='-e':
        print("Uso: python programa.py -c <cantidad de tiradas> -n <cantidad de corridas> -e <numero elegido> ")
        sys.exit(1)


are_arguments_ok()
# Obtener el número de valores de los argumentos de la línea de comandos
num_valores = int(sys.argv[2])
corridas = int(sys.argv[4])
numero_elegido = int(sys.argv[6])

# Generar los valores aleatorios entre 0 y 36 y almacenarlos en una lista
valores = [random.randint(0, 37) for _ in range(num_valores)]

# Calcular la frecuencia absoluta de cada valor
frecuencia_absoluta = {i: valores.count(i) for i in range(0,37)}



# Calcular la frecuencia relativa de cada valor
frecuencia_relativa  = {i: frecuencia_absoluta[i] / num_valores for i in range(0,37)}

y1= list()
for i in range(0,37):
    y1.append(frecuencia_relativa[i])
x1= list(range(37))

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(x1, y1, color='red')
plt.xlabel('Número de la ruleta')
plt.ylabel('Frecuencia relativa')
plt.title('Frecuencia relativa')
plt.legend()
plt.grid(True)
plt.show()


# Imprimir los resultados
print("Valores generados:", valores)
for i in range(0,37):
    print(f"Frecuencia absoluta de {i}:", frecuencia_absoluta[i])
    print(f"Frecuencia relativa de {i}:", frecuencia_relativa[i])

print(f'Numeros de corridas {corridas}, Numero elegido: {numero_elegido}')




