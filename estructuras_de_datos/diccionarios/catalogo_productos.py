'''
Tarea:
Crear un diccionario Python para representar un simple catálogo de productos. El diccionario debe contener tres productos, con el SKU (Unidad de mantenimiento de existencias) de cada producto como clave. Incluya la siguiente información como valores para cada producto:

name: El nombre del producto.

price: El precio del producto.

quantity: El número de artículos en stock.

Aquí están los (3) productos:

SKU123
nombre: Widget A
precio: 19.99
cantidad: 50

SKU456
nombre: Gadget B
precio: 34.95
cantidad: 25

SKU789
nombre: Gizmo C
precio: 9.99
cantidad: 100 100

Una vez creado el diccionario, escriba código para recuperar e imprimir el precio de un producto específico utilizando su SKU.
'''

#PRACTICA PEDRO CON MAYOR DIFICULTAD
productos = []
numero_de_productos = 0

while numero_de_productos < 1:
    sku = input("Indica los numeros del SKU: ")
    nombre = input("¿Cual es el nombre del producto?: ")
    precio = input("Cual es el precio para ese producto?: ")
    cantidad = input("Cual es la cantidad de unidades de ese producto?: ")
    
    productos.append({
    'SKU' + str(sku):{
        'name':nombre, 
        'price':precio, 
        'quantity':cantidad}
    })
    
    numero_de_productos += 1

sku_to_find = input("\nIndica el SKU a buscar (ej. SKU123): ")

encontrado = False
for producto in productos:
    if sku_to_find in producto:
        info = producto[sku_to_find]
        print(f"El precio del {info['name']} es ${info['price']}")
        encontrado = True
        break

if not encontrado:
    print("Producto no encontrado.")


#TAREA PEDIDA EN LA CERTIFICACION    

product_catalog = {
    'SKU123': {'name': 'Widget A', 'price': 19.99, 'quantity': 50},
    'SKU456': {'name': 'Gadget B', 'price': 34.95, 'quantity': 25},
    'SKU789': {'name': 'Gizmo C', 'price': 9.99, 'quantity': 100}
}

sku_to_find = "SKU123"

if sku_to_find in product_catalog:
    print(f"The price of {product_catalog[sku_to_find]['name']} is ${product_catalog[sku_to_find]['price']}")
else:
    print("Producto no encontrado.")