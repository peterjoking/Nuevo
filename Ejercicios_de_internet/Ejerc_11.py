# Ejercicio 12
"""
Write a program that takes a list of numbers
(for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and
last elements of the given list. For practice, write this code inside a function.

"""
import random
a = random.sample(range(100),10)
print(a)
def extremos_lista(lista):
    return [lista[0], lista[len(lista)-1]]


b = extremos_lista(a)
print(b)

