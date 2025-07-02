""" Desafío de programación: Adivina el número secreto
Su tarea:
Creará un juego de adivinar números en el que el ordenador intentará adivinar un número secreto que usted le indique. El ordenador generará conjeturas aleatorias dentro de un rango (1 a 10) y continuará adivinando hasta que encuentre el número correcto.

Instrucciones:
Configure su secret_number: Elija un número entre 1 y 10 y asígnele una variable llamada secret_number. No lo asigne al azar; elija un número para poder verificar que el código funciona.

Inicializa otra variable llamada guess con un valor de 0.

Completa el bucle while: Añada la condición al bucle while para asegurarse de que continúa ejecutándose mientras guess no sea igual a su secret_number.

Ejemplo de salida:
Guessing: 3

Guessing: 8

Guessing: 1

Guessing: 7

I guessed the right number! It was 7 """

# Exactamente como lo piden:
import random

secret_number = 10

guess = 0

while guess != secret_number:
    guess = random.randint(1, 10)
    print("Guessing:", guess)

print("I guessed the right number! It was", secret_number)


# Si quiero que el usuario sea el que elija el numero:
print("Adivina el numero")

numero_secreto = random.randint(1, 11)
guessed = False

while not guessed:
    guess_number = int(input("Coloca un numero del 1 al 11: "))

    if guess_number == numero_secreto:
        print("You guessed the right number! It was ", numero_secreto)
        guessed = True
    else:
        print("Guessing: ", guess_number)
