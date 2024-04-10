import random
import sys
import matplotlib.pyplot as plt
import numpy as np
import math


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
    

def generate_layout_por_corridas(corridas):
    # Create layout
    # Dividir los números en sub-listas de longitud 4
    sub_lists = [list(range(i, min(i + 4, corridas + 1))) for i in range(1, corridas + 1, 4)]

    # Completar las últimas filas con el último número repetido si es necesario
    if len(sub_lists[-1]) < 4:
        sub_lists[-1].extend([sub_lists[-1][-1]] * (4 - len(sub_lists[-1])))

    # Crear el layout final
    layout = [[str(num) for num in row] for row in sub_lists]

    fig, axd = plt.subplot_mosaic(layout)
    return fig, axd

def generate_frecuencia_relativa_plot(numeroDeTiradas, corridas, numeroElegido ,valoresAleatorios):
    valores_bases = list(range(37))
    x1 = list(range(1, numeroDeTiradas+1))
    fig, axd = generate_layout_por_corridas(corridas)
    for i in range(1, corridas+1):
        axd[f'{i}'].plot(x1, calcular_frecuencias_relativas_por_tiradas(numeroElegido, valoresAleatorios[i-1]), label='Frecuencia relativa por número de tirada', color='red')
        axd[f'{i}'].plot(x1, calcular_frecuencia_relativa_esperada(valores_bases, valoresAleatorios[i-1]), linestyle='--', label='Frecuencia relativa esperada', color='blue')
        axd[f'{i}'].set_xlabel('Número de tirada')
        axd[f'{i}'].set_ylabel('Frecuencia relativa')
        axd[f'{i}'].set_title(f'Gráfico {i}')
    fig.suptitle('Frecuencia relativa por tiradas', fontsize=16)
    plt.tight_layout()
    plt.show(block=False)


def generate_promedio_plot(numeroDeTiradas, corridas, numeroElegido, valoresAleatorios):
    valores_bases = list(range(37))
    x1 = list(range(1, numeroDeTiradas+1))
    fig, axd = generate_layout_por_corridas(corridas)
    for i in range(1, corridas+1):
        axd[f'{i}'].plot(x1, calcular_numero_promedio_por_tirada(valoresAleatorios[i-1]), label='Frecuencia relativa por número de tirada', color='red')
        axd[f'{i}'].plot(x1, calcular_promedio_esperado(valores_bases, valoresAleatorios[i-1]), linestyle='--', label='Frecuencia relativa esperada', color='blue')
        axd[f'{i}'].set_xlabel('Número de tirada')
        axd[f'{i}'].set_ylabel('Número Promedio')
        axd[f'{i}'].set_title(f'Gráfico {i}')
    fig.suptitle('Número promedio por tirada', fontsize=16)
    plt.tight_layout()
    plt.show(block=False)

def generate_desviacion_plot(numeroDeTiradas,corridas,numeroElegido,valoresAleatorios):
    valores_bases = list(range(37))
    x1 = list(range(1,numeroDeTiradas+1))
    fig, axd = generate_layout_por_corridas(corridas)
    for i in range(1,corridas+1):
        axd[f'{i}'].plot(x1, calcular_desviacion_estandar_por_tirada(valoresAleatorios[i-1],numeroElegido),label='Frecuencia relativa por número de tirada', color='red')
        axd[f'{i}'].plot(x1,calcular_desviacion_estandar_esperada(valores_bases, valoresAleatorios[i-1]),linestyle='--',label='Frecuencia relativa esperada', color='blue')
        axd[f'{i}'].set_xlabel('Número de tirada')
        axd[f'{i}'].set_ylabel('Desviación')
        axd[f'{i}'].set_title(f'Gráfico {i}')
    fig.suptitle('Desviación estándar por tiradas', fontsize=16)
    plt.tight_layout()
    plt.show(block=False)

def generate_varianza_plot(numeroDeTiradas,corridas,numeroElegido,valoresAleatorios):
    valores_bases = list(range(37))
    x1 = list(range(1, numeroDeTiradas+1))
    fig, axd = generate_layout_por_corridas(corridas)
    for i in range(1, corridas+1):
        axd[f'{i}'].plot(x1, calcular_varianza_calculada(numeroElegido, valoresAleatorios[i-1], numeroDeTiradas), label='Frecuencia relativa por número de tirada', color='red')
        axd[f'{i}'].plot(x1, calcular_varianza_esperada(valores_bases, valoresAleatorios[i-1]), linestyle='--', label='Frecuencia relativa esperada', color='blue')
        axd[f'{i}'].set_xlabel('Número de tirada')
        axd[f'{i}'].set_ylabel('Valor de varianza')
        axd[f'{i}'].set_title(f'Gráfico {i}')
    fig.suptitle('Varianza esperada vs Varianza calculada en función del número de tiradas', fontsize=16)
    plt.tight_layout()
    plt.show(block=False)

def calcular_filas(corridas):
    filas = 1
    acumulador = 0
    for i in range(1,corridas+1):
        acumulador += 1
        if acumulador > 4:
            filas += 1
            acumulador = 0
    return filas


def calcular_frecuencias_relativas_por_tiradas(numeroElegido,valoresAleatorios):
    frecuencia_absoluta = 0
    numero_tirada = 0
    frecuencias_relativas_por_tirada = []
    for numero in valoresAleatorios:
        numero_tirada += 1
        if numeroElegido == numero:
            frecuencia_absoluta += 1
        frecuencia_relativa = frecuencia_absoluta / numero_tirada
        frecuencias_relativas_por_tirada.append(frecuencia_relativa)  
    return frecuencias_relativas_por_tirada


def calcular_frecuencia_relativa_esperada(valores_bases, tiradas):
    frecuencia_relativa_esperada = 1 / len(valores_bases)
    frecuencias_relativa_recta = []
    for _ in tiradas:
        frecuencias_relativa_recta.append(frecuencia_relativa_esperada)
    return frecuencias_relativa_recta


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


def calcular_promedio_esperado(valores_bases, tiradas):
    suma = 0
    for valor in valores_bases:
        suma += valor
    promedio_esperado = suma / len(valores_bases)
    promedio_esperado_recta = []

    for _ in tiradas:
        promedio_esperado_recta.append(promedio_esperado)
    return promedio_esperado_recta


def calcular_desviacion_estandar_por_tirada(valoresAleatorios, numeroElegido):
    desviaciones_por_tirada = []
    for i in range(1, len(valoresAleatorios) + 1):
        valores_tirada = np.array(valoresAleatorios[:i])
        desviacion = np.std(valores_tirada)
        desviaciones_por_tirada.append(desviacion)
    return desviaciones_por_tirada


def calcular_desviacion_estandar_esperada(valores_bases, tiradas):
    desviacion_estandar_esperada = ((((valores_bases[-1] - valores_bases[0] + 1)**2) - 1) / 12)**0.5
    desviacion_estandar_recta = []
    for _ in tiradas:
        desviacion_estandar_recta.append(desviacion_estandar_esperada)
    return desviacion_estandar_recta


def calcular_varianza_esperada(valores_bases, tiradas):
    varianza_esperada = (((valores_bases[-1] - valores_bases[0] + 1)**2) - 1) / 12
    varianza_recta = []
    for _ in tiradas:
        varianza_recta.append(varianza_esperada)
    return varianza_recta


def calcular_varianza_calculada(numeroElegido, valoresAleatorios, numeroDeTiradas):
    valores_aleatorios = np.array(valoresAleatorios)
    varianzas_calculadas = []

    for i in range(1, numeroDeTiradas + 1):
        diferencias_cuadradas = (valores_aleatorios[:i] - numeroElegido) ** 2
        varianza_calculada = np.mean(diferencias_cuadradas)
        varianzas_calculadas.append(varianza_calculada)

    return varianzas_calculadas
