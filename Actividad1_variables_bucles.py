'''
Paso 1: Almacenar los datos de temperatura

Instrucciones:
Necesita dos listas para almacenar los datos de temperatura.

La primera lista, celsius_temperatures, ya ha sido creada.

Añada a ella las siguientes temperaturas Celsius de muestra: 0, 10, 25, 32, 100 a celsius_temperatures.

Cree la segunda lista, fahrenheit_temperatures, como una lista vacía para almacenar las temperaturas Fahrenheit convertidas más tarde. En este momento debería ser una lista vacía.

Imprime ambas listas para observar su estado inicial.

Paso 2: Convertir temperaturas

Instrucciones:
Es hora de convertir las temperaturas Celsius a Fahrenheit:

Se le ha proporcionado un bucle for para iterar a través de cada valor celsius en la lista celsius_temperatures.

Dentro del bucle:

Aplica la fórmula de conversión de Celsius a Fahrenheit: F = (C * 9/5) + 32, donde F es la temperatura Fahrenheit y C es la temperatura Celsius. Utilice la fórmula como se muestra arriba.

El código para almacenar cada valor calculado fahrenheit en la lista fahrenheit_temperatures utilizando el método append() ha sido proporcionado para usted.

Imprima los resultados.
'''

celsius_temperatures = [0, 10, 25, 32, 100]
fahrenheit_temperatures = []

print("Celsius Temperatures: ", celsius_temperatures,
      "Fahrenheit Temperatures: ", fahrenheit_temperatures)

for temperature in celsius_temperatures:
    fahrenheit = (temperature * 9/5) + 32

    fahrenheit_temperatures.append(fahrenheit)

print("Celsius Temperatures: ", celsius_temperatures,
      "Fahrenheit Temperatures: ", fahrenheit_temperatures)
