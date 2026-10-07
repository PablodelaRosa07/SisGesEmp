class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        print(f"{self.codigo} - {self.nombre} - {self.precio} € - Stock: {self.stock}")

    def reponer(self, cantidad):
        if cantidad > 0:
            self.stock += cantidad
            print(f"Se han repuesto {cantidad} unidades. Nuevo stock: {self.stock}")
        else:
            print("La cantidad a reponer debe ser mayor que 0.")

    def vender(self, cantidad):
        if cantidad <= 0:
            print("Error: La cantidad a vender debe ser mayor que 0.")
        elif cantidad > self.stock:
            print(f"Error: Stock insuficiente. Stock actual: {self.stock}")
        else:
            self.stock -= cantidad
            print(f"Venta realizada: {cantidad} unidades. Stock restante: {self.stock}")



producto1 = Producto("P001", "Monitor", 199.99, 10)

producto1.vender(-2)

producto1.vender(15)

producto1.vender(4)