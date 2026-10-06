def calcularTotal(ventas):
    total = 0
    for venta in ventas:
        total += venta
    return total

misVentas = [120.50, 80, 35.90, 220, 15]
print("Total de ventas:", calcularTotal(misVentas))