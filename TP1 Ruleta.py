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

def calcular_frecuencias_relativas_por_tiradas(numero_elegido,valores):
    frecuencia_absoluta = 0
    numero_tirada = 0
    frecuencias_relativas_por_tirada = []
    for numero in valores:
        numero_tirada +=1
        if numero_elegido == numero:
            frecuencia_absoluta +=1 
        frecuencia_relativa = frecuencia_absoluta / numero_tirada
        frecuencias_relativas_por_tirada.append(frecuencia_relativa)  
    return frecuencias_relativas_por_tirada


# Calcular la frecuencia absoluta de cada valor
frecuencia_absoluta = {i: valores.count(i) for i in range(0,37)}




# Calcular la frecuencia relativa de cada valor
frecuencia_relativa  = {i: frecuencia_absoluta[i] / num_valores for i in range(0,37)}

y1= list()
for i in range(0,37):
    y1.append(frecuencia_relativa[i])
x1= list(range(num_valores))

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(x1, calcular_frecuencias_relativas_por_tiradas(numero_elegido,valores), color='red')
plt.xlabel('Número de tirada')
plt.ylabel('Frecuencia relativa')
plt.title('Frecuencia relativa por tiradas')
plt.legend()
plt.grid(True)
plt.show()


# Imprimir los resultados
print("Valores generados:", valores)
for i in range(0,37):
    print(f"Frecuencia absoluta de {i}:", frecuencia_absoluta[i])
    print(f"Frecuencia relativa de {i}:", frecuencia_relativa[i])

print(f'Numeros de corridas {corridas}, Numero elegido: {numero_elegido}')

print(calcular_frecuencias_relativas_por_tiradas(numero_elegido,valores))