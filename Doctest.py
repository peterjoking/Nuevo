def suma(numero1,numero2):
    """
    Aqui estoy haciendo el ejercicio de ejemplo de Udemy referente a Doctest.
    Dentro de las triples comillas escribo lo que quiero tester co n3 signos "mas"
    >>> suma (3,4)
    7

    """

    return numero1 + numero2

resultado = suma (2,8)
print(resultado)

import doctest
doctest.testmod()