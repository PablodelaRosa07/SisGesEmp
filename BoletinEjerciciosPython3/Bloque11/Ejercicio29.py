importe = float(input("Introduce el importe de la compra: "))
esVipInput = input("¿El cliente es VIP? (sí/no): ").strip().lower()

esVip = esVipInput in ["sí", "si", "s"]

if esVip:
    descuento = 0.10
elif importe > 100:
    descuento = 0.05
else:
    descuento = 0.0

importeFinal = importe * (1 - descuento)

print(f"Importe final a pagar: {importeFinal} €")