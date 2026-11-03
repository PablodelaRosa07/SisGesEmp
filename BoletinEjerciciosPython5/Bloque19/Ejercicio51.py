class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        print(f"{self.codigo} - {self.nombre} - {self.precio} € - Stock: {self.stock}")

    def valor_stock(self):
        return self.precio * self.stock


producto1 = Producto("P001", "Monitor", 200, 5)

print(f"Producto: {producto1.nombre}")
print(f"Precio: {producto1.precio} €")
print(f"Stock: {producto1.stock}")

print(f"Valor del stock: {producto1.valor_stock()} €")