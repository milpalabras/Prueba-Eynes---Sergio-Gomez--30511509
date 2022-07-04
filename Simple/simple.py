import random

def generar_lista_dict():
    lista = []
    for i in range(1, 11):
        lista.append({'id': i, 'edad': random.randint(1, 100)})
    return lista

def ordenar_lista_dict(lista):
    print(min(lista, key=lambda x: x['edad'])['id'])
    print(max(lista, key=lambda x: x['edad'])['id'])

    return sorted(lista, key=lambda x: x['edad'])

ordenar_lista_dict(generar_lista_dict())