
print("Digame su nombre ")
nombre = input()

print("Cuantos años tiene?: ")
edad = input()

anospara100 = 100 - int(edad)
anos100 = 2020 + int(anospara100)
print("tendrás 100 años en el año: {}".format(anos100))

#Ejercicio 3
import datetime
ahora = datetime.datetime.now()
print("Ahora son las {} horas ".format(ahora))
