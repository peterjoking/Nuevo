#agregar una linea de texto al archivo de texto que fué creado antes.

fichero = open("archivo_prueba.txt", "at")
caracteres_agregados ='\nEsta es una línea mas de texto que fué agregada con otro programa de Python'
fichero.write(caracteres_agregados)

fichero.close()
