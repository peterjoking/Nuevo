#Ejercicio 9

"""
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low,
too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)
"""
import  random
x = str
while x !="exit":
  numeros_aleatorios = random.randint(1,9)
  user = int(input("Adivina que numero es generado aleatóriamente, entre 1 y 9:?\n"))
  if user == numeros_aleatorios:
        print("acertaste!!!!")
  else:
        print("nop, ese no es, el resuldado era {} ".format(numeros_aleatorios))
  x = input("presione 'exit' para terminar\n")

