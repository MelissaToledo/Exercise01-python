#PARTE 1: Agregar clientes
listaRegistro = []
clientes = 0
agregar = input("¿Desea iniciar a agregar clientes?: ")

while agregar == "si" :
    cliente = input("nombre del cliente: ")
    producto = input("producto: ")
    costo = float(input("costo ($0.00): "))
    agregar = input("¿Desea agregar otro cliente?: ") #aqui se define si el bucle continua o para

    # punto de programa en que definimos el diccionario
    registro = dict(cliente=cliente, producto=producto, costo=costo)
    # como agrego un elemento nuevo a una lista?
    listaRegistro.append(registro)
    # dejar de ocupar la variable registro
    # registro = None
    
    clientes += 1 #acción del bucle
print("son")
for registro in listaRegistro:
    print(registro)

#PARTE 2: Reporte del costo total 

print("El costo total hasta el momento es:")
print(registro["costo"])

for registro["costo"] in listaRegistro:
    print(costo)
