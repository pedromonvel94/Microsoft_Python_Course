""" ¿Puedes escribir un programa en Python que simule un temporizador de cuenta regresiva simple? El temporizador debe comenzar en 10 y contar hacia atrás hasta cero, imprimiendo cada número a medida que avanza. Durante la cuenta regresiva, tu programa debe verificar si el número actual es igual a 5. Si lo es, el programa debe mostrar un mensaje especial: "¡Punto medio alcanzado!".  """

punto_inicio = 10

for i in range(punto_inicio, 0, -1):
    print("Cuenta regresiva: ", i)

    if i == punto_inicio/2:
        print("¡Punto medio alcanzado!")
