while True:
    try:
        precio = float(input("Introduce el precio del producto: "))
        if precio > 0:
            print(f"Precio válido introducido: {precio} €")
            break
        else:
            print("El precio debe ser un número mayor que 0.")
    except ValueError:
        print("Error: Debes introducir un número válido.")