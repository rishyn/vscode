
repit = 1
while (repit != 0):
    cargar = int(input("\nColoque el monto q cargara: "))

    if (cargar >= 3000):
        cargar = ((cargar * 120) / 100)- 90
        print("\nEl monto total cargado es: ",cargar)
    else:
        print("\nEl monto cargado es: ",cargar)

    repit= int(input("seguir ?"))
