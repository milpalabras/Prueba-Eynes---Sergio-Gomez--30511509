import random

def generar_lista_dict():
    lista = []
    for i in range(1, 11):
        lista.append({'id': i, 'edad': random.randint(1, 100)})
    return lista