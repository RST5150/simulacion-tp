import random
import sys
import matplotlib.pyplot as plt


def are_arguments_ok():
    # Verificar si los argumentos enviados son correctos
    if len(sys.argv) != 7 or sys.argv[1] != "-c" or sys.argv[3] !='-n' or sys.argv[5]!='-e':
        print("Uso: python programa.py -c <cantidad de tiradas> -n <cantidad de corridas> -e <numero elegido> ")
        sys.exit(1)




def get_correct_arguments():
    # Obtener el número de valores de los argumentos de la línea de comandos
    num_valores = int(sys.argv[2])
    corridas = int(sys.argv[4])
    numero_elegido = int(sys.argv[6])

    return num_valores, corridas, numero_elegido



def generate_random_values(numeroDeTiradas):
    # Generar los valores aleatorios entre 0 y 36 y almacenarlos en una lista
    valores = [random.randint(0, 37) for _ in range(numeroDeTiradas)]
    return valores



def generate_plot(numeroDeTiradas,numeroElegido, valoresAleatorios):
    # Crear el gráfico
    x1= list(range(numeroDeTiradas))
    plt.figure(figsize=(10, 6))
    plt.plot(x1, calcular_frecuencias_relativas_por_tiradas(numeroElegido,valoresAleatorios),label='Frecuencia relativa por número de tirada', color='red')
    plt.plot(x1,calcular_frecuencia_relativa_esperada(numeroDeTiradas,numeroElegido,valoresAleatorios),label='Frecuencia relativa esperada', color='blue')
    plt.xlabel('Número de tirada')
    plt.ylabel('Frecuencia relativa')
    plt.title('Frecuencia relativa por tiradas')
    plt.legend()
    plt.grid(True)
    plt.show()


def calcular_frecuencias_relativas_por_tiradas(numeroElegido,valoresAleatorios):
    frecuencia_absoluta = 0
    numero_tirada = 0
    frecuencias_relativas_por_tirada = []
    for numero in valoresAleatorios:
        numero_tirada +=1
        if numeroElegido == numero:
            frecuencia_absoluta +=1 
        frecuencia_relativa = frecuencia_absoluta / numero_tirada
        frecuencias_relativas_por_tirada.append(frecuencia_relativa)  
    return frecuencias_relativas_por_tirada


def calcular_frecuencia_relativa_esperada(numeroDeTiradas,numeroElegido,valoresAleatorios):
    frecuencia_absoluta = 0
    frecuencia_relativa = []
    for numero in valoresAleatorios:
        if numero == numeroElegido:
            frecuencia_absoluta += 1
    for _ in range(numeroDeTiradas):
        frecuencia_relativa.append(frecuencia_absoluta / len(valoresAleatorios))
    return frecuencia_relativa


