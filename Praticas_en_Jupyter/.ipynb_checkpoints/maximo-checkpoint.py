"""Devuelve el número máximo de una lista"""
lista_uno =[]
lista =int(input("ingrese la cantidad de números de la lista:\n"))

for i in range(lista):
    cada_numero = int(input("ingrese los números: \n"))
    lista_uno.append(cada_numero)
    
maximo = 0
for numero in lista_uno:
    if numero > maximo: 
        maximo = numero
        
if __name__=="__main__":   
    print("la lista es: {}, y el máximo es:\n".format(lista_uno))      
    print(maximo)
