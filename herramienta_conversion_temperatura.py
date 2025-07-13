'''
Bloque de código funcional: Herramienta de conversión de temperatura
Tu tarea:
Escribir tres funciones Python que implementen una sencilla herramienta de conversión de temperatura. Ten cuidado de escribir correctamente los nombres de los métodos.

celsius_to_fahrenheit(celsius): Toma una temperatura en grados Celsius y la convierte a grados Fahrenheit.

fahrenheit_to_celsius(fahrenheit): Toma una temperatura en Fahrenheit y la convierte a Celsius.

convert_temperature(temperature, unit): Toma un valor de temperatura y una unidad ('C' para Celsius o 'F' para Fahrenheit). Llama a la función de conversión apropiada basada en la unidad y devuelve la temperatura convertida.

Asegúrese de que devuelve los valores como números en coma flotante; no redondee.

Ejemplo de uso:
temperature_c = 25
temperature_f = 77

converted_f = convert_temperature(temperature_c, 'C')
converted_c = convert_temperature(temperature_f, 'F')

print(f"{temperature_c}°C is equal to {converted_f}°F")
print(f"{temperature_f}°F is equal to {converted_c}°C")

Salida esperada:
25°C is equal to 77.0°F
77°F is equal to 25.0°C

'''

def celsius_to_fahrenheit(celsius:float) -> float:
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit:float) -> float:
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def convert_temperature(temperature, unit):
    
    if unit.lower() == "c":
        converted_f = celsius_to_fahrenheit(temperature)
        return converted_f
    elif unit.lower() == "f":
        converted_c = fahrenheit_to_celsius(temperature)
        return converted_c
            

temperature_c = 25
temperature_f = 77

converted_f = convert_temperature(temperature_c, 'C')
converted_c = convert_temperature(temperature_f, 'F')

print(f"{temperature_c}°C is equal to {converted_f}°F")
print(f"{temperature_f}°F is equal to {converted_c}°C")