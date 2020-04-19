import sqlite3

conexion = sqlite3.connect("basedatos1.db")
cursor = conexion.cursor()
cursor.execute("SELECT * FROM PERSONAS2")
personas = cursor.fetchall()

for i in personas:
    print(i)

conexion.close()


