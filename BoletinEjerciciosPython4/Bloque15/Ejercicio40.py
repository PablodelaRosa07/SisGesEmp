def aplicar_descuento(precio, descuento=0):
    return precio * (1 - descuento / 100)

print("Sin descuento (100 €): ", aplicar_descuento(100))
print("Con 10% de descuento (100 €): ", aplicar_descuento(100, 10))
print("Con 20% de descuento (250 €): ", aplicar_descuento(250, 20))