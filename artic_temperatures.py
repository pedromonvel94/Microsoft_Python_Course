'''Instrucciones:
Comience con la lista antarctic_temperatures, que contiene los registros diarios de temperatura.

Aplique la función max() a la lista antarctic_temperatures para obtener la temperatura más alta registrada.

Aplique la función min() a la lista antarctic_temperatures para determinar la temperatura más baja registrada.

Imprima las temperaturas más alta y más baja.

Calcule la temperatura media sumando todas las temperaturas de la lista antarctic_temperatures mediante la función sum() y dividiendo por el número de temperaturas, que puede determinar mediante la función len(). Redondee la temperatura media calculada a un decimal utilizando la función round().

Imprima la temperatura media redondeada.

Calcule el valor absoluto de la temperatura más fría utilizando la función abs().

Imprime el valor absoluto de la temperatura más fría.'''

antartic_temperatures = [-25.5, -28.0, -26.3, -23.8, -27.1, -24.9, -29.2]

max_temp = max(antartic_temperatures)
min_temp = min(antartic_temperatures)

print(f'La temperatura mas alta alcanzada fue: {max_temp} °C, y la mas baja fue: {min_temp} °C')

suma_temperaturas = sum(antartic_temperatures)
temperatura_media = round(suma_temperaturas/len(antartic_temperatures), 1)

print(f'La temperatura media de fue de: {temperatura_media} °C')

menor_temp_abs = abs(min_temp)
print(f'El valor absoluto de la temperatura mas baja es: {menor_temp_abs} °C')