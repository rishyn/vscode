
print("\nEl monto minimo es de 500")
cargar = 500

objetivo = int(input("\nIngrese el objetivo a llegar: "))
bonus_carga = int(input("\nIngrese el bonus de recarga %: "))
monto = 500
while (monto < objetivo):

    print("\nEl monto a cargar sera: ",cargar)


    bonus = ((cargar * bonus_carga) / 100)
    C_total = cargar + bonus
    print("\nEl monto total cargado es: ",C_total,"con un ",bonus_carga,"% de bonus de carga.")
    monto = C_total
    cargar +=1

#print("\nEl monto a cargar sera: ",cargar)
#print("\nEl monto total cargado es: ",C_total,"con un ",bonus_carga,"% de bonus de carga.")










"""
    cargar = int(input("\nColoque el monto q cargara: "))
    cargar = ((cargar * 130) / 100)
    print("\nEl monto total cargado es: ",cargar)

    repit= int(input("seguir ?"))
"""

