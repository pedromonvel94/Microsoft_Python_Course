'''
Reto de código funcional: Hacer un sándwich
Tarea:
Cree una función Python llamada make_sandwich.

Esta función debe aceptar los siguientes parámetros

bread_type (una cadena que represente el tipo de pan)

filling (una cadena para el relleno principal del sándwich)

cheese (una cadena opcional para el tipo de queso, por defecto "ninguno")

toasted (un booleano opcional que indica si el bocadillo está tostado, por defecto False)

Dentro de la función, construya una frase descriptiva sobre el sándwich que se está haciendo, incorporando todos los detalles proporcionados.

Haga que la función devuelva las frases mostradas en la sección Salida Esperada más abajo.

Consejos:
Recuerde utilizar valores por defecto para los parámetros opcionales.

Use dos sentencias if para manejar el caso del queso y el caso del tostado.

Puede usar f-strings para formatear cadenas de forma conveniente.

Asegúrese de devolver la cadena, no de imprimirla.

Ejemplo Entrada:
make_sandwich("wheat", "turkey", "cheddar", True)
make_sandwich("rye", "ham")

Salida esperada:
Hacer un sandwich de trigo tostado con pavo y queso cheddar.
Hacer un sándwich de centeno con jamón.
'''

def make_sandwich(number, bread_type, filling, cheese = None, toasted = False):
    
    if cheese == None and toasted == False:
        return f"Sándwich #{number}: preparando un sándwich de pan tipo {bread_type} con relleno de {filling}, sin queso, y no está tostado."
    elif cheese != None and toasted == False:
        return f"Sándwich #{number}: preparando un sándwich de pan tipo {bread_type} con relleno de {filling}, con queso {cheese}, y no está tostado."
    elif cheese == None and toasted == True:
        return f"Sándwich #{number}: preparando un sándwich de pan tipo {bread_type} con relleno de {filling}, sin queso, y está deliciosamente tostado."
    elif cheese != None and toasted == True:
        return f"Sándwich #{number}: preparando un sándwich de pan tipo {bread_type} con relleno de {filling}, con queso {cheese}, y está deliciosamente tostado."
    else:
        return "Algún valor está errado, verifícalos por favor"

make_sandwich(1, "blanco", "pollo", "mozzarella", False)
make_sandwich(2, "integral", "atún", "suizo", True)
make_sandwich(3, "brioche", "carne de res", "provolone", True)
make_sandwich(4, "ciabatta", "vegetales", "ninguno", False)
make_sandwich(5, "baguette", "salami")
make_sandwich(6, "masa madre", "huevo", toasted=True)
make_sandwich(7, "multigrano", "vegetales a la parrilla", "gouda", False)
make_sandwich(8, "pan plano", "tofu", cheese="havarti")
make_sandwich(9, "pan de muffin inglés", "tocineta", toasted=True)
make_sandwich(10, "focaccia", "pollo al pesto")

