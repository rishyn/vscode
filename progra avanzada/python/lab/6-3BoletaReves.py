

def boleta(net):

    lis = []

    Vbruto =  int((net * 100) / 86.25)

    retencion = (Vbruto - neto)

    lis.append(retencion)
    lis.append(Vbruto)

    return lis


neto = int(input("Por favor ingrese el valor neto de la boleta: "))

datos = boleta(neto)

print("El monto neto ingresado es:", neto , "su rentencion es:", datos[0] , "y su valor bruto es:" , datos[1] )

