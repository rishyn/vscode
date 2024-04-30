


def avg_bateo(hit,turn):
    valor = (hit/turn)*1000
    return valor
    pass





hits = int(input("Indique el numero del hits: "))

turnos = int(input("Indique la cantidad de turnos: "))


avg = int(avg_bateo(hits,turnos))

print("Con ", hits ,"hits , y ", turnos, "turnos, el promedio de bateo es ",avg )