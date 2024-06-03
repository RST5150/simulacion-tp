import random
import sys
import matplotlib.pyplot as plt
import numpy as np
import math

NUMEROS_RULETA = 37
VALORES_BASES = list(range(NUMEROS_RULETA))
ROJOS = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
NEGROS = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
SUCESION_FIB = []
historial = []

FILAS = {
    1: [1, 2, 3],
    2: [4, 5, 6],
    3: [7, 8, 9],
    4: [10, 11, 12],
    5: [13, 14, 15],
    6: [16, 17, 18],
    7: [19, 20, 21],
    8: [22, 23, 24],
    9: [25, 26, 27],
    10: [28, 29, 30],
    11: [31, 32, 33],
    12: [34, 35, 36]
}

COLUMNAS = {
    1: [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34],
    2: [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35],
    3: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
}


def are_arguments_ok():
    if len(sys.argv) != 9 and len(sys.argv) != 11:
        print("Uso: python3 main.py -c <cantidad de tiradas> -n <cantidad de corridas> [-e <numero elegido>] -s <estrategia> -a <tipo de capital>")
        sys.exit(1)

    if '-e' in sys.argv:
        try:
            indice = sys.argv.index('-e')
            numero_elegido = int(sys.argv[indice + 1])
            if numero_elegido < 0 or numero_elegido > 36:
                print("El número elegido debe estar entre 0 y 36.")
                sys.exit(1)
        except ValueError:
            print("El valor después de '-e' debe ser un número entero.")
            sys.exit(1)
        except IndexError:
            print("Falta el valor después de '-e'.")
            sys.exit(1)

    if '-s' not in sys.argv or '-a' not in sys.argv:
        print("Falta la estrategia (-s) o el tipo de capital (-a).")
        sys.exit(1)

    estrategia = sys.argv[sys.argv.index('-s') + 1]
    if estrategia not in ['m', 'd', 'f', 'p']:
        print("La estrategia debe ser 'm' (Martingala), 'd' (D’Alambert), 'f' (Fibonacci) o 'p' (Paroli).")
        sys.exit(1)

    capital = sys.argv[sys.argv.index('-a') + 1]
    if capital not in ['i', 'f']:
        print("El tipo de capital debe ser 'i' (infinito) o 'f' (finito).")
        sys.exit(1)


def get_correct_arguments():
    num_valores = int(sys.argv[2])
    corridas = int(sys.argv[4])
    estrategia = sys.argv[sys.argv.index('-s') + 1]
    capital = sys.argv[sys.argv.index('-a') + 1]

    #num_valores = 1000
    #corridas = 1
    #estrategia = 'm'
    #capital = 'i'

    if '-e' in sys.argv:
        eleccion = int(sys.argv[sys.argv.index('-e') + 1])
    else:
        eleccion = 'rojo'

    return num_valores, corridas, eleccion, estrategia, capital


def generate_random_values(numeroDeTiradas):
    valores = [random.randint(0, 36) for _ in range(numeroDeTiradas)]
    return valores


def get_cmap(n, name='hsv'):
    '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct 
    RGB color; the keyword argument name must be a standard mpl colormap name.'''
    return plt.cm.get_cmap(name, n)


def generate_all_plots(numeroDeTiradas, corridas, numeroElegido, valoresAleatorios, billetera, capital, resultados):
    x1 = list(range(1, numeroDeTiradas + 1))
    cmap = get_cmap(corridas)
    colores = ['g','r','c','m','y','k','b']
    #figura, lista_graficos = plt.subplots(nrows=2, ncols=2, figsize=(18, 6))
    #lista_graficos[0,0].plot(x1, calcular_frecuencias_relativas_apuestas(numeroDeTiradas, resultados), label = 'Frecuencia relativa ap', linestyle = '--', color = 'blue')
    #fig_fr = plt.plot(x1, calcular_frecuencias_relativas_apuestas(numeroDeTiradas, resultados), color = 'blue')
    #lista_graficos[0,1].plot(x1, mostrar_caja_inicial(numeroDeTiradas, billetera, capital), label = 'caja inicial', linestyle = '--', color = 'blue')
    plt.figure()
    fig_fr = plt.gcf()
    fig_fc = plt.gcf()
    #fig_fr.set_size_inches(12, 6)
    for i in range(1, corridas + 1):
        color = list(np.random.choice(range(256), size=3)) 
        plt.plot(x1, calcular_frecuencias_relativas_apuestas(numeroDeTiradas, resultados), color = cmap(i-1), label='Frecuencia relativa apuesta')
        #fig_fr.plot(x1, calcular_frecuencias_relativas_apuestas(numeroDeTiradas, resultados), color = cmap(i-1))
        ax = fig_fr.add_subplot(111)
        ax.set_xlabel('n (número de tiradas)')
        #fig_fr.set_xlabel('n (número de tiradas)')
        ax.set_ylabel('fr (frecuencia relativa)')
        #fig_fr.set_ylabel('fr (frecuencia relativa)')
        fig_fr.suptitle('frsa (frecuencia relativa de apuesta favorable)')
        fig_fr.legend()
        ax.grid(True)

        plt.plot(x1, calcular_flujo_caja(numeroDeTiradas, resultados, billetera), color = cmap(i-1), label='Flujo de caja')
        ax2 = fig_fc.add_subplot(111)
        ax2.set_xlabel('n (número de tiradas)')
        ax2.set_ylabel('cc (cantidad de capital)')
        fig_fc.suptitle('fc (flujo de caja)')
        fig_fc.legend()
        ax2.grid(True)

        # lista_graficos[1,0].plot(x1,)
        # lista_graficos[1,0].set_xlabel('Otro')
        # lista_graficos[1,0].set_ylabel('Otro')
        # lista_graficos[1,0].set_title('Otro')
        # lista_graficos[1,0].legend()
        # lista_graficos[1,0].grid(True)

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


def calcular_frecuencias_relativas_apuestas(numeroDeTiradas, historial):
    frecuencia_absoluta = 0
    numero_tirada = 0
    frecuencias_relativas_apuestas = []
    for i in range(numeroDeTiradas):
        numero_tirada += 1
        if i < len(historial):
            if historial[i][0] == 'G':
                frecuencia_absoluta += 1
            frecuencia_relativa = frecuencia_absoluta / numero_tirada
            frecuencias_relativas_apuestas.append(frecuencia_relativa)
        else:
            #if i == len(historial):
            #    indice_ultima_caja = i - 1
            frecuencias_relativas_apuestas.append(0)
    return frecuencias_relativas_apuestas


def calcular_flujo_caja(numeroDeTiradas, historial, billetera):
    flujo_caja = []
    for i in range(numeroDeTiradas):
        if i < len(historial):
            flujo_caja.append(historial[i][1])
        else:
            if i == len(historial):
                indice_ultima_caja = i - 1
            flujo_caja.append(historial[indice_ultima_caja][1])
    return flujo_caja


def mostrar_caja_inicial(numeroDeTiradas, billetera, capital):
    caja_inicial = []
    if capital == 'i':
        for i in range(numeroDeTiradas):
            caja_inicial.append(0)
    else:
        for i in range(numeroDeTiradas):
            caja_inicial.append(10000) # Mismo valor que apuesta_inicial hard-codeado para no pasar tanto el parametro.
    return caja_inicial


def calcular_ganancia_perdida(eleccion, valor):
    if eleccion == 'negro' and valor in NEGROS:
        return 2
    elif eleccion == 'rojo' and valor in ROJOS:
        return 2
    elif eleccion == 'c-1' and valor in COLUMNAS[1]:
        return 3
    elif eleccion == 'c-2' and valor in COLUMNAS[2]:
        return 3
    elif eleccion == 'c-3' and valor in COLUMNAS[3]:
        return 3
    elif eleccion in range(NUMEROS_RULETA) and eleccion == valor:
        return 35
    else:
        return 0


def martingala(apuesta_inicial, eleccion, valores, billetera, esInfinito):
    apuesta = apuesta_inicial
    for valor in valores:
        billetera -= apuesta
        resultado = calcular_ganancia_perdida(eleccion, valor)
        if resultado == 0:
            apuesta *= 2  # Duplica la apuesta en caso de pérdida
            historial.append(['P', billetera])
        else:
            billetera += apuesta * resultado
            apuesta = apuesta_inicial  # Vuelve a la apuesta inicial en caso de ganancia
            historial.append(['G', billetera])

        if not esInfinito and billetera < apuesta:
            historial.append(['bancarrota', billetera])
            break

    return billetera, historial


def dalambert(apuesta_inicial, eleccion, valores, billetera, esInfinito):
    capital = apuesta_inicial
    ganancias = 0
    perdidas = 0
    apuesta = apuesta_inicial
    for valor in valores:
        billetera -= apuesta
        resultado = calcular_ganancia_perdida(eleccion, valor)
        if resultado == 0:
            perdidas += 1
            apuesta += 1  # Incrementa la apuesta en 1 en caso de pérdida
            historial.append(['P', billetera])
        else:
            ganancias += resultado
            apuesta = max(apuesta - 1, apuesta_inicial)  # Reduce la apuesta en 1 en caso de ganancia, al menos hasta la apuesta inicial
            billetera += apuesta * resultado
            historial.append(['G', billetera])
        if not esInfinito and billetera < apuesta:
            historial.append(['bancarrota', billetera])
            break
    return billetera, historial


def generar_sucesion(apuesta_inicial, tiradas):
    n = apuesta_inicial
    n_menos_1 = apuesta_inicial
    n_menos_2 = 0
    for _ in range(tiradas):
        SUCESION_FIB.append(n)
        n_menos_2 = n_menos_1
        n_menos_1 = n
        n += n_menos_2


def fibonacci(apuesta_inicial, eleccion, valores, billetera, esInfinito):
    generar_sucesion(apuesta_inicial, 500) # Valor hard-codeado para no pasar tanto el parametro de tiradas, dificil de alcanzar de todos modos.
    ganancias = 0
    perdidas = 0
    apuesta_actual = apuesta_inicial
    for valor in valores:
        indice_apuesta = SUCESION_FIB.index(apuesta_actual)
        billetera -= apuesta_actual
        resultado = calcular_ganancia_perdida(eleccion, valor)
        if resultado == 0:
            perdidas += 1
            apuesta_actual = SUCESION_FIB[indice_apuesta + 1]
            historial.append(['P', billetera])
        else:
            billetera += apuesta_actual * resultado
            ganancias += resultado
            historial.append(['G', billetera])
            if indice_apuesta > 1:
                apuesta_actual = SUCESION_FIB[indice_apuesta - 2]
            else:
                apuesta_actual = SUCESION_FIB[0]
        if not esInfinito and billetera < apuesta_actual:
            historial.append(['bancarrota', billetera])
            break
    print(f"Historial length: {len(historial)}")

    return billetera, historial


def paroli(apuesta_inicial, eleccion, valores, billetera, esInfinito):
    apuesta = apuesta_inicial
    racha_victorias = 0
    for valor in valores:
        billetera -= apuesta
        resultado = calcular_ganancia_perdida(eleccion, valor)
        if resultado == 0:
            apuesta = max(apuesta / 2, apuesta_inicial) # Reduce a apuesta anterior hasta la inicial
            historial.append(['P', billetera])
            racha_victorias = 0
        else:
            billetera += apuesta * resultado
            historial.append(['G', billetera])
            racha_victorias += 1
            if racha_victorias == 3:
                apuesta = apuesta_inicial # A las tres victorias reinicia la apuesta
            else:
                apuesta *= 2  # Duplica la apuesta en caso de ganar

        if not esInfinito and billetera < apuesta:
            historial.append(['bancarrota', billetera])
            break

    return billetera, historial


def jugar_ruleta(eleccion, estrategia, capital, valoresAleatorios):
    apuesta_inicial = 100
    if capital == 'i':
        esInfinito = True
        billetera = 0
    else:
        esInfinito = False
        billetera = 10000
    if estrategia == 'm':
        billetera, resultados = martingala(apuesta_inicial, eleccion, valoresAleatorios, billetera, esInfinito)
    elif estrategia == 'd':
        billetera, resultados = dalambert(apuesta_inicial, eleccion, valoresAleatorios, billetera, esInfinito)
    elif estrategia == 'f':
        billetera, resultados = fibonacci(apuesta_inicial, eleccion, valoresAleatorios, billetera, esInfinito)
    elif estrategia == 'p':
        billetera, resultados = paroli(apuesta_inicial, eleccion, valoresAleatorios, billetera, esInfinito)
    else:
        print("Estrategia no válida.")
        sys.exit(1)

    print(f"Billetera final: {billetera}")
    print(f"Historial: {resultados}")

    return billetera, resultados
