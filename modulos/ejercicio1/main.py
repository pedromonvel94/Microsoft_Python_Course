import modulos.ejercicio1.mimath as mimath

numero = int(input("Escribe un numero de 1 a 100: "))

par_o_impar = ""

if mimath.es_par(numero) == True:
    par_o_impar = "Par"
else:
    par_o_impar = "Impar"

print("El numero es par o impar: ", par_o_impar)

print("El numero es primo?: ", mimath.es_primo(numero))


'''
Aqui continuamos con el uso de la funcion del ejemplo del curso, donde usamos la calculate_mean que creamos en mimath de la siguiente manera:
'''
my_data = [2, 4, 5, 8, 1, 9]
mean_value = mimath.calculate_mean(my_data)
print(f"Mean: {mean_value}")