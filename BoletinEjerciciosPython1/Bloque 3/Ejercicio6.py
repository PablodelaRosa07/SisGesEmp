precio = float(input("Precio del Producto: "))
cantidad = float(input("Cantidad del Producto: "))

subtotal = precio*cantidad
iva = subtotal*0.21
total = subtotal+iva

print("Subtotal: ",subtotal, "€")
print("IVA: ",iva, "€")
print("Total: ",total, "€")