from FuncionesRuleta import *
import numpy as np

#are_arguments_ok()
parametros = get_correct_arguments()
numeroDeTiradas = parametros[0]
corridas = parametros[1]
numeroElegido = parametros[2]
estrategia = parametros[3]
capital = parametros[4]

valoresAleatorios = []
print(f'Numero de tiradas: {numeroDeTiradas}')
print(f'Numero de corridas: {corridas}')
print(f'Estrategia: {estrategia}')
print(f'Tipo de capital: {capital}')

for _ in range(corridas):
  valoresAleatorios.extend(generate_random_values(numeroDeTiradas))

jugar_ruleta(numeroElegido, estrategia, capital, valoresAleatorios)

# generate_all_plots(numeroDeTiradas, corridas, numeroElegido, valoresAleatorios)
