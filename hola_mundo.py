# Hola mundo!
saludo = ["Hola, Python!", 2, 3.14, True, None]

for i in range(len(saludo)):
    print("En la posicion: " + str(i+1) + " encontramos: " + str(saludo[i]))


# Optimización de condicionales (Uso de diccionarios)
def obtener_tarifa_envio(codigo_pais):
    tarifas_envio = {
        'US': 5.00,
        'CA': 7.50,
        'MX': 6.00,
        'CO': 4.00
    }

    return tarifas_envio.get(codigo_pais, 10.00)


print("La tarifa de envio para ese pais es: ", obtener_tarifa_envio('US'))
