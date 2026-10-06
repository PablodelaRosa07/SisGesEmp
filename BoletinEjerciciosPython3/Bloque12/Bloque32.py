precios = [10, 250, 30, 150, 80, 300]

contadorCaros = 0

print("Precios superiores a 100 €:")
for precio in precios:
    if precio > 100:
        print(f"{precio} €")
        contadorCaros += 1

print(f"Número total de productos caros: {contadorCaros}")