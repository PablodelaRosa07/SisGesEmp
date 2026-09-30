clientes = [
    {"nombre": "Ana", "email": "ana@email.com", "ciudad": "Sevilla"},
    {"nombre": "Luis", "email": "luis@email.com", "ciudad": "Córdoba"},
    {"nombre": "Carlos", "email": "carlos@email.com", "ciudad": "Sevilla"},
    {"nombre": "Marta", "email": "marta@email.com", "ciudad": "Granada"},
    {"nombre": "Elena", "email": "elena@email.com", "ciudad": "Sevilla"}
]

ciudadBuscada = input("Ciudad: ")

contador = 0
for cliente in clientes:
    if cliente["ciudad"].lower() == ciudadBuscada.lower():
        contador += 1

print(f"Número de clientes de {ciudadBuscada}: {contador}")