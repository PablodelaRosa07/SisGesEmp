def calcularPrecioFinal(precio, cantidad):
    return precio * cantidad

compra1 = calcularPrecioFinal(15.50, 3)
compra2 = calcularPrecioFinal(100, 2)
compra3 = calcularPrecioFinal(4.99, 10)

print(f"Compra 1: {compra1} €")
print(f"Compra 2: {compra2} €")
print(f"Compra 3: {compra3} €")