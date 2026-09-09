# Programa para una ferretería

# Función para calcular el subtotal
def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal


# Función para aplicar el 8% de descuento
def calcular_descuento(subtotal):
    if subtotal >= 3000:
        descuento = subtotal * 0.08
    else:
        descuento = 0
    return descuento


# Función para calcular el IVA del 15% después del descuento
def calcular_iva(subtotal, descuento):
    monto_con_descuento = subtotal - descuento
    iva = monto_con_descuento * 0.15
    return iva


# Procedimiento para mostrar los resultados
def mostrar_resultado(producto, subtotal, descuento, iva):
    total = subtotal - descuento + iva

    print("\n    FACTURA    ")
    print("Producto:", producto)
    print("Subtotal: C$", round(subtotal, 2))
    print("Descuento: C$", round(descuento, 2))
    print("IVA (15%): C$", round(iva, 2))
    print("Total: C$", round(total, 2))


# Programa principal
print("=== FERRETERÍA ===")

producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: C$ "))
cantidad = int(input("Ingrese la cantidad: "))

subtotal = calcular_subtotal(precio, cantidad)
descuento = calcular_descuento(subtotal)
iva = calcular_iva(subtotal, descuento)

mostrar_resultado(producto, subtotal, descuento, iva)
