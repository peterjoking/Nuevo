import sqlite3

conexion = sqlite3.connect("basededatosdelejercicio.db")

cursor = conexion.cursor()
cursor.execute ("CREATE TABLE Productos1(id INTEGER, nombre TEXT, precio INTEGER)" )
conexion.commit()
listavarios = [(1,'impresora',300), (2, 'raton', 20), (3, 'ordenador', 600)]
cursor.executemany("INSERT INTO Productos1 VALUES (?,?,?)",listavarios)
conexion.commit()

cursor.execute("SELECT * FROM Productos1")
products = cursor.fetchall()

for i in products:
    print(i)

cursor.close()



