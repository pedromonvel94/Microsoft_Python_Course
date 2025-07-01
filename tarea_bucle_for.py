"""Desafío de código funcional: Aprovechando los bucles for

En este ejercicio, utilizarás un bucle for para mostrar valores que son divisibles entre 3 y 4. Empezarás por 0 y seguirás hasta el final. Comenzará en 0 y pasará por valor_máximo + 1. 

Algunos ejemplos:

16 es divisible en partes iguales por 4, pero no es divisible en partes iguales por 3, por lo que 16 no se imprimiría.

18 es divisible por 3, pero no por 4, por lo que 18 no se imprimirá.

19 no es divisible por ninguno de los dos, por lo que 19 no se imprimiría.

24 es divisible por 3 y 4, por lo que se imprimiría 24.

Se ha incluido un código de inicio para usted:

Una variable max_value, establecida en 50.

Tarea:

Crear un bucle for: Utilice la función range() para generar la secuencia de números. Recuerde que range(max_value + 1) incluirá max_value en el bucle.

Consejos:

Si valor_máximo se establece en 50, la salida debe incluir 0, 12, 24, 36 y 48, cada uno de ellos en una nueva línea.

Para comprobar si una variable llamada max_value es divisible por 3, compruebe si max_value % 3 == 0. 

Puede cambiar max_value para su propia exploración, pero el calificador esperará que se establezca en 50 para pasar con éxito las pruebas.

El objetivo de este ejercicio es practicar el uso de un bucle for para recorrer cada número y una sentencia if dentro del bucle para decidir si debe imprimirse. Asegúrate de que tu solución utiliza explícitamente estas estructuras fundamentales de programación para comprobar la divisibilidad de cada número de la secuencia. """

max_value = 50

for num in range(0, max_value + 1):
    if num % 3 == 0 and num % 4 == 0:
        print(num)
