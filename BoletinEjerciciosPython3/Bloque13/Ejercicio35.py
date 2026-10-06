numeroVentas = 0
totalVendido = 0.0
condicion = True
while condicion == True:
    importe = float(input("Introduce el importe de la venta (0 para terminar): "))
    
    if importe == 0:
        condicion = False
    
    numeroVentas += 1
    totalVendido += importe

print(f"Número de ventas: {numeroVentas}")
print(f"Total vendido: {totalVendido} €")