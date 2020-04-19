def positivo(numero):
    if (numero >0):
        return True
    else:
        return False


numeros =[-1, 2, 5, -10. -5, 5]

filtro = filter(positivo, numeros)

resultado = list(filtro)
print(resultado)

# continuando con otro ejercicio
import numpy as np


a = np.array ([3,4,7,6])
print(a)

type (a)