precio1 = float(input("Indica primer precio: "))
precio2 = float(input("Indica segundo precio: "))

if (precio1 > precio2):
    print("El primer precio es mayor")

elif (precio2 > precio1):
    print("El segundo precio es mayor")

else:
    print("Los precios son iguales")