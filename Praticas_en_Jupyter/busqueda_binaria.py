#In this exercise, you will implement the binary search algorithm in Python:

#Start with a list of numbers:

lista = [2, 3, 5, 8, 11, 12, 18]

#Specify the value to search_for:
search_for = 11
"""Create two variables that will represent the start and end locations of the sublist you are interested in. Initially, it will represent the start and end indices for the entire list:"""
slice_start = 0
slice_end = len(lista) - 1 
#Add a variable to indicate whether the search was successful:
found = False
"""Find the midpoint of the list, and check whether the value is greater or less than the search term. Depending on the outcome of the comparison, either finish the search or update the locations for the start/end of the sublist:"""

while slice_start <= slice_end and not found:
    location = (slice_start + slice_end) // 2
    if lista[location] == search_for:
        found = True
    else:
        if search_for < lista[location]:
            slice_end = location - 1
        else:
            slice_start = location + 1
#Check the results:
print(found)
print(location)
#You should get the following output:
#True
#4