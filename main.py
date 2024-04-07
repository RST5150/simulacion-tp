from FuncionesRuleta import *

are_arguments_ok()
parametros = get_correct_arguments()
numeroDeTiradas = parametros[0]
corridas = parametros[1]
numeroElegido = parametros[2]
valoresAleatorios = generate_random_values(numeroDeTiradas)
generate_plot(numeroDeTiradas,numeroElegido,valoresAleatorios)