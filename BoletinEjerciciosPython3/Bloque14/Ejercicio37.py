ventas = [100, -25, 50, -10, 200]

totalVentas = 0

for venta in ventas:
    if venta < 0:
        continue  
    
    totalVentas += venta

print(f"Total de ventas válidas: {totalVentas}")