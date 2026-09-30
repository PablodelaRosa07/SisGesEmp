productos = ["Teclado","Ratón","Monitor","Webcam","Impresora"]

busqueda = input("Introduce el nombre de un producto: ")

if busqueda in productos:
    print("Producto encontrado")
else:
    print("Producto no encontrado")