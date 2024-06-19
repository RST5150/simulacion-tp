from FuncionesRuleta import *
import numpy as np

are_arguments_ok()
parametros = get_correct_arguments()
numeroDeTiradas = parametros[0]
corridas = parametros[1]
eleccion = parametros[2]
estrategia = parametros[3]
capital = parametros[4]

print(f'Numero de tiradas: {numeroDeTiradas}')
print(f'Numero de corridas: {corridas}')
print(f'Eleccion: {eleccion}')
print(f'Estrategia: {estrategia}')
print(f'Tipo de capital: {capital}')
#print("Argument List:", str(sys.argv))

for i in range(corridas):
  valoresAleatorios = []
  valoresAleatorios.extend(generate_random_values(numeroDeTiradas))

  billetera, resultados = jugar_ruleta(eleccion, estrategia, capital, valoresAleatorios)

  generate_all_plots(numeroDeTiradas, corridas, eleccion, valoresAleatorios, billetera, capital, resultados, i)

generate_final_plots(numeroDeTiradas, corridas, resultados)
