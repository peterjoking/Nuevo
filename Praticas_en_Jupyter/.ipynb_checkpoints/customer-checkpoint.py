"""Crea un formato para presentar el nombre completo y ciudad de una persona"""

def format_customer(first_name, last_name, location=''):
    return first_name + " " + last_name +" "+ "(" + location + ")"

#esta opción es la del resultado
def formato_cliente(primer_nombre, apellido, ciudad=None):
    full_name = '%s %s' %(primer_nombre, apellido)
    if ciudad:
            return '%s (%s)' %(full_name, ciudad)
    else:
            return full_name
        