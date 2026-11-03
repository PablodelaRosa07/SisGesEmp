# Clase base / madre
class Persona:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email


class Cliente(Persona):
    def __init__(self, nombre, email, numero_cliente):
        super().__init__(nombre, email)
        self.numero_cliente = numero_cliente

    def mostrar_datos(self):
        print(f"Número de cliente: {self.numero_cliente}")
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")


cliente1 = Cliente("Lucía Gómez", "lucia@email.com", "C-1024")

cliente1.mostrar_datos()