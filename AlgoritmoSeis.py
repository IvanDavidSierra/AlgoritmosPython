"""
Leer los precios de los N productos comprados y calcular:
    - Total de la compra
    - Como los articulos son leidos sin IVA, se debe hacer
    se debe hacer el cálculo del IVA
    - Total de la compra + el IVA 

    Ivan Sierra 🦆

"""

numeroProductos = int(input("Digite la cantidad de productos a evaluar: "))
listaProductos = []
i = 0
iva = 0.19
productoTotal = 0
productosTotalIVA = 0


print("Digite el valor de los productos")
while i < numeroProductos:
    productos = int(input("> "))
    listaProductos.append(productos)
    i += 1 


for producto in listaProductos:
    #Calcular productos sin el IVA
    productoTotal += producto
    
    #Aplicar el IVA a cada producto
    productosIVA = producto * iva
    productosIVA = producto + productosIVA

    #Calcular total de productos con el IVA ya calculado
    productosTotalIVA += productosIVA


print("Total de la compra sin IVA: ",productoTotal)
print("Total de la compra con IVA: ",productosTotalIVA)
    