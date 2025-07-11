'''
Ejercicio 5: Ámbito de aplicación
Instrucciones
En este ejemplo, explorará el concepto de alcance.

1. Ejecute el código siguiente y observe el error. La primera llamada a una función, display_color_works(), se ejecutará correctamente. La segunda, display_color_failure(), resultará en un NameError.

2. Hay varias maneras de corregir esto.

     a. Una forma es comentar la línea que llama a display_color_failure. Esto no soluciona el problema, pero evita el error.

     b. La forma preferida es establecer shirt_color fuera de la función display_color_works, en el programa principal, y pasar el valor a ambas funciones.

     c. Una tercera forma es atrapar el error utilizando un bloque try/catch.

     d. Una cuarta forma es declarar la variable como una variable global, pero como se discutió en una lectura anterior, esto se considera una mala práctica.

3. Comente la llamada a la función display_color_failure y vuelva a ejecutar el programa. Comprueba que el error desaparece.  

def display_color_works():
  shirt_color = "Pink"
  print("First shirt color is:", shirt_color)
  
def display_color_failure():
  # Try to access 'color' directly (this will cause an error)
  print("Your shirt color is:", shirt_color)

# The shirt_color variable is in scope in this function
display_color_works()

# The shirt_color variable is not in scope in this function
display_color_failure()
'''

def display_color_works(shirt_color):
  print("First shirt color is:", shirt_color)
  
def display_color_failure(shirt_color):
  print("Your shirt color is:", shirt_color)
  
shirt_color = "Pink"

# The shirt_color variable is in scope in this function
display_color_works(shirt_color)

# The shirt_color variable is not in scope in this function
display_color_failure(shirt_color)