precio = float(input("Introduce el precio del producto: "))

if precio < 20:
    print("Producto económico")
elif 20 <= precio <= 100:
    print("Precio medio")
else:
    print("Producto de precio elevado")