"""
Write a function that takes an ordered list of numbers (a list where the elements are in order
 from smallest to largest) and another number. The function decides whether or not the given number
is inside the list and returns (then prints) an appropriate boolean.
"""


"""
def in_list(list,s):
min=0
max=len(list)-1
while(min<=max):
mid = (min+max) // 2
if(list[mid] == s):
return True
if list[mid] < s:
min = mid+1
else:
max = mid-1
return False

"""
"""
#!/Users/Jiwesh/AppData/Local/Programs/Python/Python36/python.exe
import random

def search(randset,usrnum):
    start_index = 0
    end_index = len(randset) - 1
    while True:
        middle_index = int((end_index + start_index) / 2)
        middle_element = randset[middle_index]
        if middle_element == usrnum or randset[start_index]==usrnum or randset[end_index]==usrnum:
            return True
            break
        if middle_index == start_index or middle_index == end_index or middle_index == 0:
            return False
            break
        elif middle_element > usrnum:
            end_index = middle_index
        else:
            start_index = middle_index

    
#a=random.sample(range(1,30),random.randint(10,20))
b=[1,2,5,7,9,12,13,15,17,19,21,24,25,27,33,34,37,39]

usrinput=int(input("Please enter your search number>>> "))
if(search(b,usrinput)):
    print("your number is in the set..")
else:
    print("Your number is not in the list...")

print("The set is ")
print(b)"""

"""
 Let’s take the list a = [1, 3, 5, 30, 42, 43, 500]. It is an “ordered list”, or a list where the elements in the list go from smaller to larger. Let’s say we want to know whether the element 9 is in the list or not. Here is what we do:

Look at the middle element in the list - it is ‘30’. * ‘9 < 30’, so let us ignore the elements to the right of ‘30’.
The new list we are looking at is now [1, 3, 5].
Look at the middle element in this new list - it is 3.
‘9 > 3’, so ignore the elements to the left of 3.
The new list we are looking at is [5].
The list has one element and it is not 9.
9 is not in the list.
"""
import random

def buscar(lista, numero_usuario):
    star_index = 0
    end_index = len(lista)-1
    while True:
        mitad_indice = int((end_index - star_index)/2)
        elemento_del_medio = lista[mitad_indice]
        if elemento_del_medio == numero_usuario or lista[star_index] == numero_usuario or lista[end_index] == numero_usuario:
            return True


        if mitad_indice == star_index or mitad_indice == end_index or mitad_indice == 0:
            return False

        elif elemento_del_medio > numero_usuario:
             end_index = mitad_indice
        else:
             star_index = mitad_indice



if __name__=="__main__":
    a =random.sample(range(1,30),random.randint(5,10))
    print(a)
#para ordenar la lista uso un algoritmo
    b = sorted(a)
    usrinput = int(input("Ingrese el número a buscar:\n>>> "))
    if (buscar(b,usrinput)):
       print ("tu numero esta en la memoria")
    else:
       print ("tu número no está en la lista")

    print("los números eran: \n")
    print(b)
