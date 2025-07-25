import mimath

numero = int(input("Escribe un numero de 1 a 100: "))

par_o_impar = ""

if mimath.es_par(numero) == True:
    par_o_impar = "Par"
else:
    par_o_impar = "Impar"

print("El numero es par o impar: ", par_o_impar)

print("El numero es primo?: ", mimath.es_primo(numero))