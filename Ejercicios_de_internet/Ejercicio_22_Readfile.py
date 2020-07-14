"""
Opening a file for reading is the same as opening for writing, just using a different flag:

  with open('file_to_read.txt', 'r') as open_file:
    all_text = open_file.read()
Note how the 'r' flag stands for “read”. The code sample from above
 reads the entire open_file all at once into the all_text variable.
  But, this means that we now have a long string in all_text that
   can then be manipulated in Python using any string methods you want.

Another way of reading data from the file is line by line:

  with open('file_to_read.txt', 'r') as open_file:
  	line = open_file.readline()
  	while line:
    	print(line)
    	line = open_file.readline()
"""
"""with open('Docuprueba.txt', 'r') as open_file:
    all_text = open_file.read()

print(all_text)
"""
ruta = '/Users/Pedro/Nuevo/fichero1.txt'
with open(ruta, 'r') as open_file:
    all_text = open_file.read()

print(all_text)