#iniciamos las variables
ahorro = 0
consulta  = True

#iniciamos el ciclo while

while consulta == True:
    valor = int(input("Ingrese el monto q desea ahorrar: "))

    ahorro += valor

    respuesta = input("Desea continuar 'S' o 'N' : ")

    if respuesta == 'S':
        consulta = True

    else:
        consulta = False

print("El monto ahorrado es: ",ahorro)

