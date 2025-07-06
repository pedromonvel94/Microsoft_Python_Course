'''¡Hola! Soy tu Coach de Coursera. En esta sesión, te guiaré en el proceso de escribir una función en Python para calcular el área de un rectángulo. Exploraremos el propósito y la estructura de las funciones, sus beneficios y practicaremos la escritura de tu propia función. Para tener éxito, participa activamente: pregunta, haz sugerencias y habla sobre las áreas en las que podrías tener dificultades.  Recuerda, este es un espacio seguro para aprender y los errores son parte del proceso.

Los puntos de control para esta actividad son:

Definición de la función: Definir la función con los parámetros correctos. (Peso = 30%)
Cálculo del área: Escribir el código dentro de la función para calcular el área. (Peso = 40%)
Documentación: Añadir una cadena de documentación (docstring) que explique la función. (Peso = 20%)
Pruebas: Probar la función con diferentes valores. (Peso = 10%)
Puedes pausar en cualquier momento y verificar tu progreso. ¿Estás listo para comenzar?'''

'''Las variables que seran usadas como parametros de la funcion: '''
base = float(input("Introduce el valor de la base del rectángulo: "))
altura = float(input("Introduce el valor de la altura del rectángulo: "))

def calculo_area(base, altura):
    '''Cacular el area de un rectangulo es igual a su base * altura, los cuales son los parametros que estamos recibiendo. Estos a su vez fuera de la funcion son las variables de ambito global que poseen el input que permite al usuario ingresar su numero deseado.
    
    Args: 
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.
    
    Returns:
        float: El área del rectángulo calculada como base * altura.
    '''
 
    if base > 0 and altura > 0:
        area = base * altura
    else:
        raise ValueError("La base y la altura deben ser números positivos.")
    return area

'''Llamada a la función con los valores introducidos por el usuario'''
area_rectangulo = calculo_area(base, altura) 
print(f"El área del rectángulo es: {area_rectangulo}")