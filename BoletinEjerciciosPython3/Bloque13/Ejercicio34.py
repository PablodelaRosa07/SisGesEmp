opcion = ""

while opcion != "3":
    print("MENÚ")
    print("1. Mostrar mensaje")
    print("2. Mostrar fecha ficticia")
    print("3. Salir")
    
    opcion = input("Selecciona una opción: ").strip()

    if opcion == "1":
        print("¡Hola! Estás aprendiendo Python.")
    elif opcion == "2":
        print("Fecha ficticia: 01/01/2030")
    elif opcion == "3":
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Inténtalo de nuevo.")