import random
import sys
import matplotlib.pyplot as plt
import numpy as np
import math

NUMEROS_RULETA = 37
VALORES_BASES = list(range(NUMEROS_RULETA))


def are_arguments_ok():
    # Verificar si los argumentos enviados son correctos
    if len(sys.argv) != 7 or sys.argv[1] != "-c" or sys.argv[3] != '-n' or sys.argv[5] != '-e':
        print("Uso: python programa.py -c <cantidad de tiradas> -n <cantidad de corridas> -e <numero elegido> ")
        sys.exit(1)

    # Verificar si el valor después de "-e" está dentro del rango 0-36
    try:
        numero_elegido = int(sys.argv[6])
        if numero_elegido < 0 or numero_elegido > 36:
            print("El número elegido debe estar entre 0 y 36.")
            sys.exit(1)
    except ValueError:
        print("El valor después de '-e' debe ser un número entero.")
        sys.exit(1)


are_arguments_ok()


def get_correct_arguments():
    # Obtener el número de valores de los argumentos de la línea de comandos
    num_valores = int(sys.argv[2])
    corridas = int(sys.argv[4])
    numero_elegido = int(sys.argv[6])

    return num_valores, corridas, numero_elegido


def generate_random_values(numeroDeTiradas):
    # Generar los valores aleatorios entre 0 y 36 y almacenarlos en una lista
    valores = [random.randint(0, 36) for _ in range(numeroDeTiradas)]
    return valores


def get_cmap(n, name='hsv'):
    '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct 
    RGB color; the keyword argument name must be a standard mpl colormap name.'''
    return plt.cm.get_cmap(name, n)


def generate_all_plots(numeroDeTiradas, corridas, numeroElegido, valoresAleatorios):
    x1= list(range(1,numeroDeTiradas+1))
    cmap = get_cmap(corridas)
    colores=['g','r','c','m','y','k','b']
    figura, lista_graficos = plt.subplots(nrows=2, ncols=2, figsize=(18, 6))
    lista_graficos[0,0].plot(x1,calcular_frecuencia_relativa_esperada(numeroDeTiradas),label='Frecuencia relativa esperada',linestyle='--',color='blue')
    lista_graficos[0,1].plot(x1,calcular_promedio_esperado(numeroDeTiradas),label='Promedio esperado',linestyle='--',color='blue')
    lista_graficos[1,0].plot(x1,calcular_desviacion_estandar_esperada(numeroDeTiradas),label='Desviación estándar esperada',linestyle='--',color='blue')
    lista_graficos[1,1].plot(x1,calcular_varianza_esperada(numeroDeTiradas),label='Varianza esperada',linestyle='--',color='blue')
    for i in range(1,corridas+1):
        color = list(np.random.choice(range(256), size=3)) 
        lista_graficos[0,0].plot(x1, calcular_frecuencias_relativas_por_tiradas(numeroElegido,valoresAleatorios[i-1]), color=cmap(i-1))
        lista_graficos[0,0].set_xlabel('Número de tirada')
        lista_graficos[0,0].set_ylabel('Frecuencia relativa')
        lista_graficos[0,0].set_title('Frecuencia relativa por tiradas')
        lista_graficos[0,0].legend()
        lista_graficos[0,0].grid(True)

        lista_graficos[0,1].plot(x1,calcular_numero_promedio_por_tirada(valoresAleatorios[i-1]), color=cmap(i-1))
        lista_graficos[0,1].set_xlabel('Número de tirada')
        lista_graficos[0,1].set_ylabel('Número')
        lista_graficos[0,1].set_title('Promedio por tiradas')
        lista_graficos[0,1].legend()
        lista_graficos[0,1].grid(True)

        lista_graficos[1,0].plot(x1,calcular_desviacion_estandar_por_tirada(valoresAleatorios[i-1],numeroElegido), color=cmap(i-1))
        lista_graficos[1,0].set_xlabel('Número de tirada')
        lista_graficos[1,0].set_ylabel('Número')
        lista_graficos[1,0].set_title('Desviacion estandar por tiradas')
        lista_graficos[1,0].legend()
        lista_graficos[1,0].grid(True)

        lista_graficos[1, 1].plot(x1, calcular_varianza_calculada(numeroElegido, valoresAleatorios[i-1], numeroDeTiradas),color=cmap(i-1))
        lista_graficos[1, 1].set_ylabel('Valor de varianza')
        lista_graficos[1, 1].set_title('Varianza esperada vs Varianza calculada en función del número de tiradas')
        lista_graficos[1, 1].legend()
        lista_graficos[1, 1].grid(True)

    plt.tight_layout()
    plt.show()


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


def calcular_frecuencia_relativa_esperada(numeroDeTiradas):
    frecuencia_relativa_esperada = 1 / NUMEROS_RULETA
    frecuencias_relativa_recta = []
    for _ in range(numeroDeTiradas):
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


def calcular_promedio_esperado(numeroDeTiradas):
    suma = 0
    promedio_esperado_recta = []
    for valor in range(NUMEROS_RULETA):
        suma += valor
    promedio_esperado = suma / NUMEROS_RULETA
    for _ in range(numeroDeTiradas):
        promedio_esperado_recta.append(promedio_esperado)
    return promedio_esperado_recta


def calcular_desviacion_estandar_por_tirada(valoresAleatorios, numeroElegido):
    desviaciones_por_tirada = []
    for i in range(1, len(valoresAleatorios) + 1):
        valores_tirada = np.array(valoresAleatorios[:i])
        desviacion = np.std(valores_tirada)
        desviaciones_por_tirada.append(desviacion)
    return desviaciones_por_tirada


def calcular_desviacion_estandar_esperada(tiradas):
    desviacion_estandar_esperada = ((((VALORES_BASES[-1] - VALORES_BASES[0] + 1)**2) - 1) / 12)**0.5
    desviacion_estandar_recta = []
    for _ in range(tiradas):
        desviacion_estandar_recta.append(desviacion_estandar_esperada)
    return desviacion_estandar_recta


def calcular_varianza_esperada(tiradas):
    varianza_esperada = (((VALORES_BASES[-1] - VALORES_BASES[0] + 1)**2) - 1) / 12
    varianza_recta = []
    for _ in range(tiradas):
        varianza_recta.append(varianza_esperada)
    return varianza_recta


def calcular_varianza_calculada(numeroElegido, valoresAleatorios, numeroDeTiradas):
    promedio = calcular_promedio_esperado(numeroDeTiradas)
    valores_aleatorios = np.array(valoresAleatorios)
    varianzas_calculadas = []

    for i in range(1, numeroDeTiradas + 1):
        diferencias_cuadradas = (valores_aleatorios[:i] - promedio[-1]) ** 2
        varianza_calculada = np.mean(diferencias_cuadradas)
        varianzas_calculadas.append(varianza_calculada)

    return varianzas_calculadas
