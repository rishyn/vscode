def calcular_total_con_descuento(precios, descuento):
    total = sum(precios)
    descuento_porcentaje = descuento / 100
    descuento_monto = total * descuento_porcentaje
    total_con_descuento = total - descuento_monto
    return total, total_con_descuento

# Solicitar precios al usuario
precios = []
precio = float(input("Ingrese los precios de los artículos (ingrese 0 para finalizar): "))

while precio != 0:

    precios.append(precio)
    precio = float(input("Ingrese los precios de los artículos (ingrese 0 para finalizar): "))

# Solicitar descuento al usuario
descuento_valido = False
while not descuento_valido:
    descuento = input("Ingrese el descuento (en porcentaje, máximo 50%): ")
    if descuento.replace('.', '', 1).isdigit():
        descuento = float(descuento)
        if 0 <= descuento <= 50:
            descuento_valido = True
        else:
            print("El descuento debe ser un valor entre 0% y 50%.")
    else:
        print("Ingrese un valor numérico válido.")

# Calcular total con descuento
total, total_con_descuento = calcular_total_con_descuento(precios, descuento)

# Imprimir resultado
print(f"El total a pagar sin descuento es: ${total:.2f}")
print(f"El total a pagar con un descuento del {descuento}% es: ${total_con_descuento:.2f}")