'''
Pregunta 3
Ejercicio 3: Sin parámetros, pero con valor de retorno
Instrucciones
En este ejemplo, crearás una función para generar un número de la suerte. Al declararla como una función, este código puede ser reutilizado en otras partes del programa. Al tener la definición en un solo lugar, le permitiría cambiar la funcionalidad en muchos lugares cambiando una línea en la función.

Comience escribiendo la definición de función para una función get_lucky_number. Recuerde, esta función no debe requerir ningún parámetro de entrada (una línea de código). Evite las sugerencias de tipo para el valor de retorno.

A continuación, la función debe devolver el valor de lucky_num (una línea de código). El valor ya ha sido cargado; su tarea es devolver el valor al programa principal.

Ejecute el programa. Se generará un número aleatorio en el rango (1 a 100, como se define en la función). Esto permite escribir la lógica una vez y reutilizarla muchas veces en el programa.
'''
import random

def get_lucky_number():
    lucky_num = random.randint(1,100)
    
    return lucky_num

lucky_number = get_lucky_number()

print("Your lucky number is:", lucky_number)