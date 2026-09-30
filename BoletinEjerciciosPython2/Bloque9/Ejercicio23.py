clientes = [
    {"nombre": "Ana", "email": "ana@email.com", "ciudad": "Sevilla"},
    {"nombre": "Luis", "email": "luis@email.com", "ciudad": "Córdoba"},
    {"nombre": "Marta", "email": "marta@email.com", "ciudad": "Granada"}
]

emailBuscado = input("Introduce un email: ")

clienteEncontrado = None

for cliente in clientes:
    if cliente["email"].lower() == emailBuscado.lower():
        clienteEncontrado = cliente
        break

if clienteEncontrado:
    print("Cliente encontrado:")
    print(f"Nombre: {clienteEncontrado['nombre']}")
    print(f"Ciudad: {clienteEncontrado['ciudad']}")
else:
    print("No existe ningún cliente con ese email.")