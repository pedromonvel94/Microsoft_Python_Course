import pandas as pd
import numpy as np

def calculate_mean(data):
    return np.mean(data) 
''' 
En este módulo, hemos definido una función llamada calculate_mean que aprovecha la biblioteca NumPy (np) para calcular la media de una lista de números.
'''

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
def es_primo(numero):
    if numero <= 1:
        return False
    
    for i in range(2, int(numero**0.5) + 1 ): #Desde 2 hasta la raiz cuadrada de numero +1 (**0.5 es como decir √(numero))
        if numero % i == 0:
            return False        
    return True

