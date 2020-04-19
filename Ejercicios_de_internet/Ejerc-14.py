#Ejercicio 14

"""
Write a program (function!) that takes a list and returns a new list that contains all
 the elements of the first list minus all the duplicates.
"""

names = set()
names.add("Michele")
names.add("Robin")
names.add("Michele")
print(names)


def rectificar(lista):
     lista = set(lista)
     lista = list(lista)
     return lista

a = [1,2,3,3,3,5]
b= rectificar(a)
print(b)

#usando a loop
def otro(x):
     y =[]
     for i in x:
          if i not in y:
            y.append(i)
     return y


#def rectificar2(x): return list(set(x))

