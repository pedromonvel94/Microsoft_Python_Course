'''Escribir una función Python con un nombre descriptivo preciso, como calculate_diameter_circle, incorporando al mismo tiempo un caso de serpiente.

La función debe tomar un argumento: radius (con una pista de tipo float).

Debe calcular el diámetro de un círculo (diámetro = radius * 2) y devolverlo. ASí como no hay ningún requisito para que el radio sea un número entero, usted debe asumir un retorno de float. Se le han dado instrucciones de que si el usuario envía un radio negativo, la función debe devolver -1 para indicar un error, ya que un radio negativo no es una situación común. 

Incluya un docstrip claro e informativo que explique el propósito de la función, los argumentos y el valor de retorno, utilizando también sugerencias de tipo.

Consejos:
Siga la guía de convenciones de nomenclatura (snake_case).

Asegúrese de que su docstring está bien formateado y es fácil de entender, incluyendo sugerencias de tipo.

Mantenga su función concisa y enfocada.

No realice ninguna entrada; limítese a definir la función.

Ejemplo de entrada:
Con valores simples radius = 7 y radius = 2.5.

Con casos extremos como radius = 0, radius = -3, y un valor grande como radius = 1000000.

Salida esperada:
Radius: 7, Diameter: 14

Radius: 2.5, Diameter: 5.0

Radius: 0, Diameter: 0

Radius: -3, Diameter: -1

Radius: 1000000, Diameter: 2000000'''

def calculate_diameter_of_a_circle(radius):
    '''
    The idea of this function is to calculate the diameter of any circle we send.
    
    Args: 
        radius: The radius of a circle and should be a Float.
    
    Returns:
        - first return is -1, and we get it when the user puts a negative redius, so it's a way to say that the argument recieved is wrong.
        - Second return is the diameter, we get it when the user puts a right value on the radius.

    Example:
        - calculate_diameter_of_a_circle(7)
        returns 14
    '''
    
    if radius < 0:
        return -1
    else: 
        diameter = float(radius*2)
        
        return diameter
    

test_cases = [7, 2.5, 0, -3, 1000000]

for num in test_cases:
    print(f"Radius: {num}, Diameter: ", calculate_diameter_of_a_circle(num))