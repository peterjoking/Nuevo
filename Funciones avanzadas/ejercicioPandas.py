import pandas as pd
import numpy as np

minimo = 10
maximo = 40
numero= 3

alumnos = np.random.randint(minimo, maximo, numero)

clases = ['Clase1', 'Clase2', 'Clase3']
serie = pd.Series(alumnos, index=clases)
print(serie)