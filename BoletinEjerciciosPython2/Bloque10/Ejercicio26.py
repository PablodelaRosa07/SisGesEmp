clientesTiendaA = {"Ana", "Luis", "Marta", "Carlos"}
clientesTiendaB = {"Marta", "Carlos", "Lucía"}

todosLosClientes = clientesTiendaA | clientesTiendaB
print("Todos los clientes:", todosLosClientes)

clientesComunes = clientesTiendaA & clientesTiendaB
print("Clientes en ambas tiendas:", clientesComunes)

soloTiendaA = clientesTiendaA - clientesTiendaB
print("Clientes solo en la tienda A:", soloTiendaA)