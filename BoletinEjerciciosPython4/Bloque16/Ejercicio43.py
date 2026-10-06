def productoMasCaro(productos):
    masCaro = productos[0]
    
    for producto in productos:
        if producto["precio"] > masCaro["precio"]:
            masCaro = producto
            
    return masCaro

productos = [
    {"nombre": "Teclado", "precio": 25},
    {"nombre": "Monitor", "precio": 180},
    {"nombre": "Ratón", "precio": 15}
]

resultado = productoMasCaro(productos)
print("El producto más caro es:", resultado)