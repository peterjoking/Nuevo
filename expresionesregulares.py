import re

def buscar (palabra, texto):
    resultado = re.search(palabra,texto)
    return resultado

texto = "Este es un texto donde escribo algo para después probar un programa en el cual voy a buscar una palabra"
palabra = input('coloque la palabra que quiere buscar: \n')

resultado = buscar(palabra,texto)

if (resultado):
    print("La palabra {} fuén econtrada dentro del texto: {}".format(palabra, texto))
    inicial = resultado.start()
    final = resultado.end()
    print("\ncomienza en {} y termina en la posición {}".format(inicial, final))
else:
    print("Palabra {} no encontrada".format(palabra))

