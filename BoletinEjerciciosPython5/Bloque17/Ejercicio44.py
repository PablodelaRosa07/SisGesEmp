try:
    edad = int(input("Introduce tu edad: "))
    print(f"Edad introducida: {edad}")
except ValueError:
    print("Debes introducir un número entero.")