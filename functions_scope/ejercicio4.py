'''
Ejercicio 4: Parámetros y valor de retorno  
Instrucciones
En este ejemplo, usted escribirá una función para calcular el total descontado basado en si un usuario es miembro del club de descuentos o no.

Empiece escribiendo la definición de la función calc_sale_price. Esta función aceptará dos parámetros de entrada (una línea de código). El primero, amount, es un número que representa el importe de la compra. El segundo, member, es una variable booleana que representa si el usuario es socio (True) o no (False). Evite las sugerencias de tipo para los parámetros y el tipo de retorno.

Redondee amount a dos decimales utilizando la función integrada round. Guarde el resultado en la variable amount.

La función debe devolver el valor de amount. 

Ejecute el código. Se mostrarán los importes descontados.
'''

def calc_sale_price(amount:float, member:bool):
	if member:
		# Members receive a 15% discount (0.15)
		amount = amount - (amount * 0.15)
	else:
		# Non-members get a 5% discount (0.05)
		amount = amount - (amount * 0.05)

	amount = round(amount)

	return amount

full_price = 150.50

# Call function for members
member_price = calc_sale_price(full_price, True)
print("Member price:",member_price)

# Call function for non-members
non_member_price = calc_sale_price(full_price, False)
print("Non-member price:",non_member_price)