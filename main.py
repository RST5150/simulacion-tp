from FuncionesRuleta import *

are_arguments_ok()
parametros = get_correct_arguments()
numeroDeTiradas = parametros[0]
corridas = parametros[1]
numeroElegido = parametros[2]
valoresAleatorios = generate_random_values(numeroDeTiradas)
print(f'Numero elegido:{numeroElegido}')
print(f'Numero de tiradas:{numeroDeTiradas}')
print(f'Numero de corridas:{corridas}')
print(valoresAleatorios)
generate_all_plots(numeroDeTiradas,numeroElegido, valoresAleatorios)