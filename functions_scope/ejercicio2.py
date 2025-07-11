'''
Ejercicio 2: Parámetros, pero sin valor de retorno  
Instrucciones
En este ejemplo, usted escribirá una función que toma dos parámetros y mostrará un mensaje personalizado.

El código inicial tiene una llamada a una función, happy_birthday, que usted escribirá.

Escriba la definición de la función, happy_birthday, que toma dos parámetros, el primero llamado age y el segundo llamado name (1 línea de código). Evite las sugerencias de tipo para los parámetros.

La función debe imprimir Happy Birthday <name> and congratulations on turning <age> years old! para el usuario (1 línea de código). Por ejemplo, si pasa los valores 22 para la edad y Nora para el nombre, el programa debe mostrar Happy Birthday Nora and congratulations on turning 22 years old!. La función no debe devolver ningún valor. Asegúrese de que el espaciado es coherente con los requisitos (por ejemplo, "Feliz cumpleaños Nora" tiene dos espacios entre "Cumpleaños" y "Nora" cuando debería tener uno).

Ejecute el programa. ASÍ COMO ESTÁ ESCRITO, siempre mostrará el mismo mensaje, pero podría modificarse para aceptar entradas en lugar de utilizar siempre los mismos valores.
'''

def happy_birthday(age, name):
    print(f"Happy Birthday {name} and congratulations on turning {age} years old!")


happy_birthday(22, "Nora")