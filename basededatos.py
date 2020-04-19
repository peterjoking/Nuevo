import sqlite3
conexion = sqlite3.connect("basedatos1.db")

cursor = conexion.cursor()
cursor.execute ("CREATE TABLE PERSONAS2(nombre TEXT, apellido TEXT, edad INTEGER)" )
cursor.execute("INSERT INTO PERSONAS2 VALUES('Pedro', 'Lopez', 44)")
lista_varios = [('Pablo', 'Alvares', 32), ('Gimena', 'Rodriguez', 21), ('Michele', 'Miranda', 41), ('Alejandra', 'Ritrovato', 28)]

cursor.executemany("INSERT INTO PERSONAS2 VALUES (?,?,?)",lista_varios)
conexion.commit()
conexion.close()
