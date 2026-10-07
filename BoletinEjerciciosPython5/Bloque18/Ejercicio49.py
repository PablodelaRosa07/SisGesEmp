class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        print(f"{self.codigo} - {self.nombre} - {self.precio} € - Stock: {self.stock}")

    def reponer(self, cantidad):
        self.stock += cantidad


producto1 = Producto("P001", "Monitor", 199.99, 5)

print(f"Stock inicial: {producto1.stock}")

reposicion = 3
producto1.reponer(reposicion)
print(f"Reposición: {reposicion}")

print(f"Stock final: {producto1.stock}")