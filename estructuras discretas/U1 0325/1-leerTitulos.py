
file = open("title.basics.tsv", "r")

i = 0
palabra = set()
data = dict()

i = 0

for line in file:
    arr = line.strip().lower().split("\t")
    if i>1:
        data.update({arr[0]:arr[2]})
        palabras_titulo=arr[2].split(" ")
        palabra.update(set(palabras_titulo))
    i+= 1

#close de files
file.close()
