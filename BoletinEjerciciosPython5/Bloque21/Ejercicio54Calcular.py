def calcular_iva(precio, porcentaje=21):
    return precio * (porcentaje / 100)


def calcular_descuento(precio, porcentaje):
    return precio * (porcentaje / 100)


def calcular_total(precio, descuento=0, porcentaje_iva=21):
    precio_con_descuento = precio - calcular_descuento(precio, descuento)
    iva = calcular_iva(precio_con_descuento, porcentaje_iva)
    return precio_con_descuento + iva