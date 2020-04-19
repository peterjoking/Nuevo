import pickle
frutas = {'v':'verde', 'r': 'rojo', 'a':'azul', 'n':'negro'}

fichero = open('fichero.pckl', 'wb')

pickle.dump(frutas, fichero)

fichero.close()


fichero2 = open('fichero.pckl', 'rb')
diccionario = pickle.load(fichero2)

print(diccionario)
frutas.values()

