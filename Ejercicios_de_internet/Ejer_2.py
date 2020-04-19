#Ejercicio 2
"""
numero = input("ingrese un numero \n")
if (int(numero) % 2 ==0):
    print("El número es par ")
else:
    print("el número es impar")

"""
#Ejercicio 3

"""
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5."""
"""
lista = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for elemento in lista:
   if (elemento < 5):
       print(lista[elemento])
"""

#Ejerc 4
"""
Create a program that asks the user for a number and then prints out 
a list of all the divisors of that number. (If you don’t know what a divisor is,
 it is a number that divides evenly into another number. For example,
  13 is a divisor of 26 because 26 / 13 has no remainder.)"""

numero = int(input("ingrese un numero para dividir: \n"))

intervalo = list(range(1, numero+1))
listado =[]
for num in intervalo:
    if (numero % num ==0):
          listado.append(num)
print(listado)

"""
num1 = int(input("Please choose a number to divide: "))

listRange = list(range(1,num1+1))

divisorList = []

for number in listRange:
    if num1 % number == 0:
        divisorList.append(number)

print(divisorList)
"""
