'''
Ejercicio 6: Importar un módulo  
Instrucciones
En este ejemplo, examinarás el uso de funciones de otro módulo.

Usted ha creado un archivo llamado menus.py almacenado en la misma carpeta que su programa actual. Este módulo contiene una función, display_menu, que ha sido escrita. No toma argumentos y devuelve un valor numérico.

Importa el módulo menus para que su contenido esté disponible en tu programa.

Introduzca el código para llamar al módulo display_menu en el módulo de menús. El resultado se guardará en la variable user_choice.

Este código requiere un archivo menus.py. Funcionará en la plataforma Coursera, pero no funcionaría en un editor de código separado en su sistema. Diseñar de esta manera permite a otro programador modificar el módulo de menús independientemente de su código, y su programa se beneficiará de la última actualización.
'''
import menus

user_choice = menus.display_menu()
print("You chose option:", user_choice)




