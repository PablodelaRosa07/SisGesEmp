clientes = [
    {
        "nombre": "Ana",
        "email": "ana@email.com",
        "ciudad": "Sevilla"
    },
    {
        "nombre": "Luis",
        "email": "luis@email.com",
        "ciudad": "Córdoba"
    },
    {
        "nombre": "Marta",
        "email": "marta@email.com",
        "ciudad": "Granada"
    }
]

for cliente in clientes:
    print(f"Cliente: {cliente['nombre']} | Email: {cliente['email']} | Ciudad: {cliente['ciudad']}")