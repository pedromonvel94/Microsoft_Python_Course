""" #Tu tarea:
Escribir un programa Python que calcule el precio final de un artículo después de aplicar un descuento.

- El precio original del artículo es de 75$.

- El descuento es del 15%.

Su programa debe:

- Almacenar el precio original y el descuento en variables.

- Calcular el descuento dividiendo discount_rate entre 100 y multiplicando por precio_original.

- Calcular el precio final restando discount de precio_original. 

- Imprima el precio final con un mensaje claro.

Resultado esperado:
El precio final después del descuento es: $63.75 """

precio_original = 75
descuento = 0.15

valor_descuento = precio_original * descuento

precio_final = precio_original - valor_descuento

print("El precio final es: $", precio_final)
