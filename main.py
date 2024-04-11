from FuncionesRuleta import *
import numpy as np

are_arguments_ok()
parametros = get_correct_arguments()
numeroDeTiradas = parametros[0]
corridas = parametros[1]
numeroElegido = parametros[2]
valoresAleatorios = []
print(f'Numero elegido:{numeroElegido}')
print(f'Numero de tiradas:{numeroDeTiradas}')
print(f'Numero de corridas:{corridas}')

for _ in range(corridas):
  valoresAleatorios.append(generate_random_values(numeroDeTiradas))
generate_all_plots(numeroDeTiradas,corridas,numeroElegido,valoresAleatorios)