# Ejercicio 15

"""
Write a program (using functions!) that asks the user for a long string
containing multiple words. Print back to the user the same string, except with the
words in backwards order. For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
"""

frase = input("ingrese la oración que vamos a dar vuelta ")

lista_frase = frase.split(" ")
lista_invertida = lista_frase[::-1]
frase_invertida = " ".join(lista_invertida)
print(frase_invertida)

def invertir_palabra():
    return " ".join(frase.split() [::-1])

