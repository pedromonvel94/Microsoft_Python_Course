'''Diferencia entre return y yield:'''

#return:

def generaPares(limite):
    num = 1
    miLista = []
    
    while num <= limite:
        miLista.append(num * 2)
        num += 1
    return miLista

print(generaPares(10))

#yield:

def generadorPares(limite):
    num = 1

    while num <= limite:
        yield num * 2
        num += 1

devuelvePares = generadorPares(10)

# Con next el generador devuelve el primer elemento de un objeto iterable
print(next(devuelvePares))

# Para devolver todo el objeto iterable, elemento por elemento, es necesario usar un bucle for o while:
for i in devuelvePares:
    print(i)