import random
import matplotlib.pyplot as plt
import argparse
from collections import defaultdict


def ruleta():
    numeros = list(range(1, 37))
    return random.choice(numeros)


def es_apuesta_ganada(numero_ganador, tipo_apuesta, valor_apuesta):
    if tipo_apuesta == 'numero':
        return numero_ganador == valor_apuesta, 37
    elif tipo_apuesta == 'color':
        rojos = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
        negros = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}
        if valor_apuesta == 'rojo':
            return numero_ganador in rojos, 2
        elif valor_apuesta == 'negro':
            return numero_ganador in negros, 2
    elif tipo_apuesta == 'fila':
        filas = {
            'primera': range(1, 35, 3),
            'segunda': range(2, 36, 3),
            'tercera': range(3, 37, 3)
        }
        return numero_ganador in filas[valor_apuesta], 3
    return False, 0


def estrategia_martingala(tiradas, capital_infinito, monto_inicial, tipo_apuesta, valor_apuesta, apuesta_inicial):
    capital = monto_inicial
    historial_capital = []
    frecuencia_ganadora = []
    monto_apuesta = apuesta_inicial
    tiradas_para_ganar = 0

    for _ in range(tiradas):
        numero_ganador = ruleta()
        tiradas_para_ganar += 1
        capital -= monto_apuesta

        gano, cuanto = es_apuesta_ganada(numero_ganador, tipo_apuesta, valor_apuesta)
        if gano:
            capital += monto_apuesta * cuanto
            monto_apuesta = apuesta_inicial
            frecuencia_ganadora.append(tiradas_para_ganar)
            tiradas_para_ganar = 0
        else:
            monto_apuesta *= 2
            if not capital_infinito and capital < monto_apuesta:
                break
        historial_capital.append(capital)

    return historial_capital, frecuencia_ganadora


def estrategia_dalembert(tiradas, capital_infinito, monto_inicial, tipo_apuesta, valor_apuesta, unidad):
    capital = monto_inicial
    historial_capital = []
    frecuencia_ganadora = []
    monto_apuesta = unidad
    tiradas_para_ganar = 0

    for _ in range(tiradas):
        numero_ganador = ruleta()
        tiradas_para_ganar += 1
        capital -= monto_apuesta

        gano, cuanto = es_apuesta_ganada(numero_ganador, tipo_apuesta, valor_apuesta)
        if gano:
            capital += monto_apuesta * cuanto
            monto_apuesta = max(unidad, monto_apuesta - unidad)
            frecuencia_ganadora.append(tiradas_para_ganar)
            tiradas_para_ganar = 0
        else:
            monto_apuesta += unidad
            if not capital_infinito and capital < monto_apuesta:
                break
        historial_capital.append(capital)

    return historial_capital, frecuencia_ganadora


def estrategia_fibonacci(tiradas, capital_infinito, monto_inicial, tipo_apuesta, valor_apuesta, apuesta_inicial):
    capital = monto_inicial
    historial_capital = []
    frecuencia_ganadora = []
    secuencia_fibonacci = [1, 1]
    monto_apuesta = secuencia_fibonacci[0]
    tiradas_para_ganar = 0
    indice_fibonacci = 0

    for _ in range(tiradas):
        numero_ganador = ruleta()
        tiradas_para_ganar += 1
        capital -= monto_apuesta

        gano, cuanto = es_apuesta_ganada(numero_ganador, tipo_apuesta, valor_apuesta)
        if gano:
            capital += monto_apuesta * cuanto
            indice_fibonacci = max(0, indice_fibonacci - 2)
            monto_apuesta = secuencia_fibonacci[indice_fibonacci]
            frecuencia_ganadora.append(tiradas_para_ganar)
            tiradas_para_ganar = 0
        else:
            indice_fibonacci += 1
            if indice_fibonacci >= len(secuencia_fibonacci):
                secuencia_fibonacci.append(secuencia_fibonacci[-1] + secuencia_fibonacci[-2])
            monto_apuesta = secuencia_fibonacci[indice_fibonacci]
            if not capital_infinito and capital < monto_apuesta:
                break
        historial_capital.append(capital)

    return historial_capital, frecuencia_ganadora


def estrategia_paroli(tiradas, capital_infinito, monto_inicial, tipo_apuesta, valor_apuesta, apuesta_inicial):
    capital = monto_inicial
    historial_capital = []
    frecuencia_ganadora = []
    monto_apuesta = apuesta_inicial
    tiradas_para_ganar = 0
    victorias_consecutivas = 0

    for _ in range(tiradas):
        numero_ganador = ruleta()
        tiradas_para_ganar += 1
        capital -= monto_apuesta

        gano, cuanto = es_apuesta_ganada(numero_ganador, tipo_apuesta, valor_apuesta)
        if gano:
            capital += monto_apuesta * cuanto
            frecuencia_ganadora.append(tiradas_para_ganar)
            tiradas_para_ganar = 0
            if victorias_consecutivas < 3:
                monto_apuesta *= 2
                victorias_consecutivas += 1
            else:
                monto_apuesta = apuesta_inicial
                victorias_consecutivas = 0
        else:
            monto_apuesta = apuesta_inicial
            victorias_consecutivas = 0
            if not capital_infinito and capital < monto_apuesta:
                break
        historial_capital.append(capital)

    return historial_capital, frecuencia_ganadora

def main():
    parser = argparse.ArgumentParser(description='Simulación de Ruleta Americana con Estrategias de Apuesta')
    parser.add_argument('-c', type=int, required=True, help='Cantidad de tiradas')
    parser.add_argument('-n', type=int, required=True, help='Cantidad de corridas')
    parser.add_argument('-e', type=int, help='Número elegido')
    parser.add_argument('-d', type=str, help='Color o fila elegida')
    parser.add_argument('-s', type=str, required=True, choices=['m', 'd', 'f', 'p'],
                        help='Estrategia (m: Martingala, d: D\'Alembert, f: Fibonacci)')
    parser.add_argument('-a', type=str, required=True, choices=['i', 'f'],
                        help='Tipo de capital (i: infinito, f: finito)')
    parser.add_argument('-m', type=int, help='Monto de billetera inicial')
    parser.add_argument('-x', type=int, help='Apuesta inicial')

    args = parser.parse_args()

    tipo_apuesta = None
    valor_apuesta = None
    if args.e is not None:
        tipo_apuesta = 'numero'
        valor_apuesta = args.e
    elif args.d is not None:
        if args.d in ['rojo', 'negro']:
            tipo_apuesta = 'color'
            valor_apuesta = args.d
        elif args.d in ['primera', 'segunda', 'tercera']:
            tipo_apuesta = 'fila'
            valor_apuesta = args.d
        else:
            raise ValueError("Valor de -d no válido")
    else:
        raise ValueError("Debe especificar -e o -d")

    capital_infinito = args.a == 'i'
    if capital_infinito:
        monto_inicial = 0
    else:
        monto_inicial = args.m
    apuesta_inicial = args.x

    resultados_historial = []
    resultados_frecuencia = []

    if args.s == 'm':
        estrategia = estrategia_martingala
        nombre = 'Martingala'
    elif args.s == 'd':
        estrategia = estrategia_dalembert
        nombre = 'Dalember'
    elif args.s == 'f':
        estrategia = estrategia_fibonacci
        nombre = 'Fibonacci'
    elif args.s == 'p':
        estrategia = estrategia_paroli
        nombre = 'Paroli'

    if capital_infinito:
        capital_infinito_nombre = 'infinito'
    else:
        capital_infinito_nombre = 'finito'

    # Crear subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    for i in range(args.n):
        historial_capital, frecuencia_ganadora = estrategia(args.c, capital_infinito, monto_inicial, tipo_apuesta,
                                                            valor_apuesta, apuesta_inicial)
        if not frecuencia_ganadora:
            frecuencia_ganadora.append(-1)
        resultados_historial.append(historial_capital)
        resultados_frecuencia.append(frecuencia_ganadora)

    # Añadir línea rayada en el monto inicial de la cartera
    if capital_infinito:
        ax1.axhline(y=0, color='r', linestyle='--', linewidth=2, zorder=10, label='Monto inicial')
    else:
        ax1.axhline(y=monto_inicial, color='r', linestyle='--', linewidth=2, zorder=10, label='Monto inicial')

    # Graficar historial de capital
    for j, resultado in enumerate(resultados_historial):
        ax1.plot(resultado, label=f'Corrida {j + 1}')
        ax1.plot(len(resultado) - 1, resultado[-1], 'o', color='black', zorder=10)

    ax1.set_xlabel('Número de tiradas')
    ax1.set_ylabel('Monto')
    ax1.set_title(f'Historial de Capital estrategia: {nombre}, con capital {capital_infinito_nombre}')
    ax1.legend()
    # Graficar frecuencia relativa de éxito acumulada
    colores = plt.cm.get_cmap('tab10', args.n)

    for j, frecuencia_ganadora in enumerate(resultados_frecuencia):
        frecuencia_total = defaultdict(int)
        total_tiradas = len(frecuencia_ganadora)

        for tirada in frecuencia_ganadora:
            frecuencia_total[tirada] += 1

        tiradas = sorted(frecuencia_total.keys())
        frecuencias_relativas = [frecuencia_total[tirada] / total_tiradas for tirada in tiradas]

        ax2.bar(tiradas, frecuencias_relativas, width=1, edgecolor="black", linewidth=0.7, alpha=0.2,
                label=f'Corrida {j + 1}')

    # Ajustar el rango del eje X para mostrar todos los números enteros excluyendo el cero
    max_tirada = max(tiradas)
    ax2.set_xlim(left=0.5, right=max_tirada + 0.5)
    ax2.set_xticks(range(1, max_tirada + 1))

    ax2.set_xlabel('Número de tiradas hasta ganar')
    ax2.set_ylabel('Frecuencia relativa')
    ax2.set_title('Frecuencia relativa de obtener la apuesta ganadora')
    ax2.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
