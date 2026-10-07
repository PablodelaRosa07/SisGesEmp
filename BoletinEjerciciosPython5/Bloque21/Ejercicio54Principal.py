# Importamos las funciones del módulo calculos.py
from Ejercicio54Calcular import calcular_descuento, calcular_iva, calcular_total

precio_base = 100.0
porcentaje_descuento = 10

monto_iva = calcular_iva(precio_base)
monto_descuento = calcular_descuento(precio_base, porcentaje_descuento)
total_final = calcular_total(precio_base, descuento=porcentaje_descuento)

print(f"Precio base: {precio_base} €")
print(f"IVA (21%): {monto_iva} €")
print(f"Descuento ({porcentaje_descuento}%): {monto_descuento} €")
print(f"Total a pagar: {total_final} €")