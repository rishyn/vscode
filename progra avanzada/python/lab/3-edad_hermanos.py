
#juan Ana y Carlos

edad_juan = int(input("Por favor introduzca la edad de Juan "))

edad_ana = int (input("Porfavor introduzcala edad de Ana "))

edad_carlos = int(input("Porfavor introduzcala edad de Carlos "))

if edad_juan > edad_ana and edad_juan > edad_carlos:
    print(" Juan es mayor q Ana y Carlos")
else:
    if edad_ana > edad_juan and edad_ana > edad_carlos:
        print(" Ana es mayor q Juan y Carlos")

    else:
        print(" Carlos es mayor q Ana y Juan")
