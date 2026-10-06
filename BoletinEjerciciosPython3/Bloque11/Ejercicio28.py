stockDisponible = int(input("Introduce el stock disponible: "))
cantidadDeseada = int(input("Introduce la cantidad que quiere comprar el cliente: "))

if cantidadDeseada <= stockDisponible:
    print("Venta posible")
else:
    print("Stock insuficiente")