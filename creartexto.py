# Programa para crear un archivo de texto.

fichero = open('archivo_prueba.txt','wt')
texto_del_fichero = "Este un texto que fué creado a través del programa python usando\n el programa PyChar"

fichero.write(texto_del_fichero)
fichero.close()
