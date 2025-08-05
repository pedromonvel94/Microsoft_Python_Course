'''
Reto de programación: Carrito de la compra
Su tarea:
Escribir un programa en Python que almacene una lista de artículos en un carrito de la compra utilizando una estructura de datos mutable y, a continuación, imprima el contenido del carrito.

Crea una lista llamada shopping_cart para almacenar los elementos, ya que permite añadir y eliminar elementos fácilmente.

Añade los siguientes elementos a la lista utilizando tres métodos distintos append:
manzana
plátano
leche

Nota: Esto también se podría hacer con el método extend, pero este ejemplo se centra en el método más común append.

Utilice un bucle for para recorrer cada item en la lista shopping_cart e imprimir cada elemento. Asegúrese de utilizar el nombre de variable item para cada elemento de la lista. Asegúrese de no utilizar ninguna función adicional.
'''

shopping_cart = []

shopping_cart.append('Manzana')
shopping_cart.append('Platano')
shopping_cart.append('Leche')

for item in shopping_cart:
    print(item) 