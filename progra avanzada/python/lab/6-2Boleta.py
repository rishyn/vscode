



def boleta(brut):


    lis = []

    retencion = int((brut * 13.75)/100)
    neto = (brut - retencion)

    lis.append(retencion)
    lis.append(neto)

    return lis



bruto = int(input("Por favor introduzca el valor bruto de la boleta: "))

datos = boleta(bruto)

print("El monto bruto ingresado es:",bruto, "su retencion es:", datos[0] ,"y su valor neto es:",datos[1] )

