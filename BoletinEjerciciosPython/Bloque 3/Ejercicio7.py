precioOriginal = float(input("Precio del Producto: "))
porcentajeDescuento = float(input("Porcentaje de Descuento: "))

importeDescontado = precioOriginal*(porcentajeDescuento/100)
precioTotal = precioOriginal-importeDescontado

print("Precio original: ",precioOriginal, "€")
print("Porcentaje de Descuento: ",porcentajeDescuento, "%")

print("Importe descontado: ",importeDescontado, "€")
print("Precio Final: ",precioTotal, "€")