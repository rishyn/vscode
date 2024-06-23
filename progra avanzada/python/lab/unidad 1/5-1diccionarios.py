#definir diccionarios

peliculas = { "Kill Bill" : "Quentine Tarantino" , "Star Wars" : "George Lucas" }

print(peliculas)

print(peliculas[ "Star Wars" ])


peliculas2= { "Kill Bill" : [ "2023" , "Quentin Tarantino" , "Miramax" ] , "Star Wars" : [ "1977" , "George Lucas", "Lucas Film" ]}

print(peliculas2[ "Kill Bill" ])



# anadir al diccionario

nombre  = input("Por favor ingrese el nombre de la pelicula: " )
director = input("Por favor ingrese el nombre completo del director: " )

peliculas [nombre] = director
print(peliculas)

#para modificar una lista se repite el mismo proceso de arriba

#   //



#eliminar una pelicula del diccionario

nombre = input("Que pelicula desea eliminar: ")
del(peliculas[nombre])

print(peliculas)

# pero q pasa si la pelicula a eliminar no esta en la lista para esto se usa esta funcion

nombre = input("Que pelicula desea eliminar: ")

if nombre in peliculas.keys():
    del(peliculas[nombre])
    print(peliculas)

else:
    print ("La pelicula " + nombre + " no existe en el diccionario")



