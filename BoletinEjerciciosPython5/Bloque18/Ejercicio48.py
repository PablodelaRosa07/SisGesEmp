class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        print(f"{self.codigo} - {self.nombre} - {self.precio} € - Stock: {self.stock}")


producto1 = Producto("P001", "Monitor", 199.99, 8)

producto1.mostrar_info()