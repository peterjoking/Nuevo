import modulofichero

nombre_fichero = 'fichero1.txt'
fichero = modulofichero.Fichero(nombre_fichero)

texto = 'Esto es el ejemplo de escritura a través de un programa que utiliza el \nmodulo de otro programa' \
        ' estoy probando varias líneas'
fichero.grabar_fichero(texto)
texto = '\nEste es otra linea con otro texto que fué agregado'

fichero.incluir_texto(texto)

texto_leido = fichero.leer_fichero()
print (texto_leido)
