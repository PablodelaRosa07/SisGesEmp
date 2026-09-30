productos = ["Teclado", "Ratón", "Monitor"]

productos.append("Webcam")
productos.append("Altavoces")
productos.remove("Ratón")

indice_monitor = productos.index("Monitor")
productos[indice_monitor] = "Monitor 27 pulgadas"

print("Lista final de productos:", productos)