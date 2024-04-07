from FuncionesRuleta import *
import numpy as np

are_arguments_ok()
parametros = get_correct_arguments()
numeroDeTiradas = parametros[0]
corridas = parametros[1]
numeroElegido = parametros[2]
valoresAleatorios = generate_random_values(numeroDeTiradas)
print(f'Numero elegido:{numeroElegido}')
print(f'Numero de tiradas:{numeroDeTiradas}')
print(f'Numero de corridas:{corridas}')
print(f'Promedio de numeros: {np.average(valoresAleatorios)}')
print(valoresAleatorios)
generate_all_plots(numeroDeTiradas,numeroElegido, valoresAleatorios)