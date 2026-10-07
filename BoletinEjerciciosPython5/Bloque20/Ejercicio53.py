class Persona:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email


class Cliente(Persona):
    def __init__(self, nombre, email, numero_cliente):
        super().__init__(nombre, email)
        self.numero_cliente = numero_cliente


class ClienteVIP(Cliente):
    def __init__(self, nombre, email, numero_cliente, descuento):
        super().__init__(nombre, email, numero_cliente)
        self.descuento = descuento  
    def calcular_precio(self, precio):
        precio_final = precio * (1 - self.descuento / 100)
        return precio_final



cliente_vip = ClienteVIP("Elena Torres", "elena@email.com", "VIP-001", 15)

precio_original = 100.0
precio_con_descuento = cliente_vip.calcular_precio(precio_original)

print(f"Cliente VIP: {cliente_vip.nombre}")
print(f"Descuento asignado: {cliente_vip.descuento}%")
print(f"Precio original: {precio_original} €")
print(f"Precio final tras descuento: {precio_con_descuento} €")