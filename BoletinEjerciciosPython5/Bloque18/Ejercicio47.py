class Cliente:
    def __init__(self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre} | Email: {self.email} | Teléfono: {self.telefono}")


cliente1 = Cliente("Ana López", "ana@email.com", "600123456")
cliente2 = Cliente("Carlos Gómez", "carlos@email.com", "655987654")

cliente1.mostrar_datos()
cliente2.mostrar_datos()