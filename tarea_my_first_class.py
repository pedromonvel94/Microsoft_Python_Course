'''

Reto de código funcional: ¡Un perro puede ladrar!
Su tarea:
Crear una clase Python llamada Dog.

Define dos atributos dentro de la clase Dog: name (una cadena para almacenar el nombre del perro) y breed (una cadena para almacenar la raza del perro).

Implementa un método llamado bark() dentro de la clase Dog. Este método debe imprimir un mensaje en la consola que incluya el nombre y la raza del perro: 
Woof! My name is name and I'm a breed.
Comprueba que el punto aparece al final de la impresión.

(proporcionado) Crea una instancia (objeto) de la clase Dog, llámala my_dog. Como no forma parte de la clase Perro, no tendrá sangría. 

(proporcionado) Utilizando la instancia de la variable my_dog. llame al método bark(), proporcionando el nombre Buddy  y la raza Golden Retriever ¡para verlo en acción!

Consejos:
Recuerde utilizar el método __init__ para inicializar los atributos name y breed al crear un nuevo objeto Dog.

Dentro del método bark(), utiliza self.name y self.breed para acceder a los atributos del perro como parte de tu sentencia print. Pero recuerda que ya están asignados 

Ejemplo de entrada (proporcionado):
my_dog = Dog("Buddy", "Golden Retriever")

my_dog.bark()

Salida esperada:
¡Guau! Me llamo Buddy y soy un Golden Retriever.
'''

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"Woof! My name is {self.name} and I'm a {self.breed}.")
        

my_dog = Dog("Buddy", "Golden Retriever")

my_dog.bark()