
paises =[]
i = 1


while i < 6:
    print("ingrese el pais N°",i)
    pais = input()
    paises.append(pais)
    i += 1

print("Lista original: ", paises)

paises.sort()


print(paises)


p_eliminar = input(print("Pais a eliminar"))


validar1 = paises.count(p_eliminar)


if validar1 == 0:
    print("Pais no c puede eliminar por q no esta en la lista")
else:
    paises.remove(p_eliminar)

print(paises)