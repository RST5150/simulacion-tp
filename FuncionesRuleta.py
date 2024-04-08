import random
import sys
import matplotlib.pyplot as plt
import numpy as np


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
    

def generate_all_plots(numeroDeTiradas,numeroElegido, valoresAleatorios):
    x1= list(range(1,numeroDeTiradas+1))
    figura, lista_graficos = plt.subplots(nrows=2,ncols=2,figsize=(18, 6))
    lista_graficos[0,0].plot(x1, calcular_frecuencias_relativas_por_tiradas(numeroElegido,valoresAleatorios),label='Frecuencia relativa por número de tirada', color='red')
    lista_graficos[0,0].plot(x1,calcular_frecuencia_relativa_esperada(numeroDeTiradas,numeroElegido,valoresAleatorios),linestyle='--',label='Frecuencia relativa esperada', color='blue')
    lista_graficos[0,0].set_xlabel('Número de tirada')
    lista_graficos[0,0].set_ylabel('Frecuencia relativa')
    lista_graficos[0,0].set_title('Frecuencia relativa por tiradas')
    lista_graficos[0,0].legend()
    lista_graficos[0,0].grid(True)


    lista_graficos[0,1].plot(x1,calcular_numero_promedio_por_tirada(valoresAleatorios),label='Promedio por número de tirada', color='red')
    lista_graficos[0,1].plot(x1,calcular_promedio_esperado(valoresAleatorios),linestyle='--',label='Promedio esperado', color='blue')
    lista_graficos[0,1].set_xlabel('Número de tirada')
    lista_graficos[0,1].set_ylabel('Número')
    lista_graficos[0,1].set_title('Promedio por tiradas')
    lista_graficos[0,1].legend()
    lista_graficos[0,1].grid(True)

    lista_graficos[1,0].plot(x1,calcular_desviacion_estandar_por_tirada(valoresAleatorios,numeroElegido),label='Desviación del número X por tirada', color='red')
    lista_graficos[1,0].plot(x1,calcular_desviacion_estandar_esperada(valoresAleatorios),linestyle='--',label='Desviación estandar esperada', color='blue')
    lista_graficos[1,0].set_xlabel('Número de tirada')
    lista_graficos[1,0].set_ylabel('Número')
    lista_graficos[1,0].set_title('Promedio por tiradas')
    lista_graficos[1,0].legend()
    lista_graficos[1,0].grid(True)

    lista_graficos[1, 1].plot(x1, calcular_varianza_calculada(numeroElegido, valoresAleatorios, numeroDeTiradas), label='Varianza calculada', color='red')
    lista_graficos[1, 1].axhline(y=calcular_varianza_esperada(numeroElegido, valoresAleatorios), color='blue', linestyle='--', label='Varianza esperada')
    lista_graficos[1, 1].set_xlabel('Número de tirada')
    lista_graficos[1, 1].set_ylabel('Valor de varianza')
    lista_graficos[1, 1].set_title('Varianza esperada vs Varianza calculada en función del número de tiradas')
    lista_graficos[1, 1].legend()
    lista_graficos[1, 1].grid(True)

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


def calcular_numero_promedio_por_tirada(valoresAleatorios):
    numeroDeTirada = 0
    suma = 0
    promedios = []
    for numero in valoresAleatorios:
        numeroDeTirada += 1
        suma = suma + numero
        promedio = int(suma / numeroDeTirada)
        promedios.append(promedio)
    return promedios


def calcular_promedio_esperado(valoresAleatorios):
    promedio = int(np.average(valoresAleatorios))
    promedioEsperado = []
    for _ in range(len(valoresAleatorios)):
        promedioEsperado.append(promedio)
    return promedioEsperado


def calcular_desviacion_estandar_por_tirada(valoresAleatorios, numeroElegido):
    desviaciones_por_tirada = []
    for i in range(1, len(valoresAleatorios) + 1):
        valores_tirada = np.array(valoresAleatorios[:i])
        desviacion = np.std(valores_tirada)
        desviaciones_por_tirada.append(desviacion)
    return desviaciones_por_tirada


def calcular_desviacion_estandar_esperada(valoresAleatorios):
    desviaciones = []
    desviacionEstandar = np.std(valoresAleatorios)
    print(f'Desviacion estandar {desviacionEstandar}')
    for _ in range(len(valoresAleatorios)):
        desviaciones.append(desviacionEstandar)
    return desviaciones


def calcular_varianza_esperada(numeroElegido, valoresAleatorios):
    valores_aleatorios = np.array(valoresAleatorios)

    diferencias_cuadradas = (valores_aleatorios - numeroElegido) ** 2

    varianza_esperada = np.mean(diferencias_cuadradas)

    return varianza_esperada


def calcular_varianza_calculada(numeroElegido, valoresAleatorios, numeroDeTiradas):
    valores_aleatorios = np.array(valoresAleatorios)
    varianzas_calculadas = []

    for i in range(1, numeroDeTiradas + 1):
        diferencias_cuadradas = (valores_aleatorios[:i] - numeroElegido) ** 2
        varianza_calculada = np.mean(diferencias_cuadradas)
        varianzas_calculadas.append(varianza_calculada)

    return varianzas_calculadas
