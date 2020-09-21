ruta1 = '/Users/Pedro/Google Drive/Practicas/Registro_Udemy_Formulario.txt'
ruta_nuevo = '/Users/Pedro/Google Drive/Practicas/nuevacopia.txt'
f = open(ruta1, "r")
new_file = open (ruta_nuevo, 'w')

for line in f:
    new_file.write(line)
f.close()
new_file.close()


"""
with open (ruta1) as f:
    with open(ruta_nuevo, 'w') as f2:
        for line in f:
            f2.write(line)


"""