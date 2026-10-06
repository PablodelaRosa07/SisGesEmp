def buscar_producto(productos, nombre):
    return nombre in productos

listaProductos = ["Teclado", "Monitor", "Ratón"]

print(buscar_producto(listaProductos, "Monitor")) 
print(buscar_producto(listaProductos, "Webcam"))   