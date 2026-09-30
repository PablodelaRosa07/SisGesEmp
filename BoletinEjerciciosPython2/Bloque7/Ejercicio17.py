producto = ("P001", "Teclado", 21)

print("Código:", producto[0])
print("Nombre:", producto[1])
print("Tipo de IVA:", producto[2])

try:
    producto[0] = "P002"
except TypeError as error:
    print("Error al intentar modificar:", error)

# Ocurre un error de tipo TypeError, lo que significa que sus elementos no se
# pueden modificar, añadir ni eliminar una vez que la tupla ha sido creada.