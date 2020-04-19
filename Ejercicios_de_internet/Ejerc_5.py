#Ejercicio N°5

"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only
the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.
"""

lista1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

lista3 = []

for numero in lista1:
    if numero in lista2:
       lista3.append(numero)

print(lista3)

#otra forma mas genérica:

import random

a = range(1, random.randint(1,30))
b = range(1, random.randint(10,50))
nueva_lista = []

for num in a:
    if num in b:
        nueva_lista.append(num)
print(nueva_lista)

#Ejercicio N6
"""
Ask the user for a string and print out whether this string is a palindrome or not.
 (A palindrome is a string that reads the same forwards and backwards.)
"""
"""
palabra = input("ingrese una palabra\n")
if palabra[::-1] == palabra:
    print("es un palindrome")
else:
    print("no es un palindrme")
"""

#Ejercicio 7
"""
Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
"""
"""
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [numero for numero in a if numero %2 ==0]

print (b)
"""

import random

otro = []

largo_lista = random.randint(5,35)
while len(otro) < largo_lista:
    otro.append(random.randint(1,75))

eventlist = [numero for numero in otro if numero % 2 ==0]
print(" el listado es: {}".format(otro))
print("el listado llamado eventlist es : {}".format (eventlist))
