import numpy as np

def es_grupo(conjunto, operacion):
    def cerradura():
        for a in conjunto:
            for b in conjunto:
                if operacion(a, b) not in conjunto:
                    return False
        return True

    def asociatividad():
        for a in conjunto:
            for b in conjunto:
                for c in conjunto:
                    if operacion(operacion(a, b), c) != operacion(a, operacion(b, c)):
                        return False
        return True

    def encontrar_identidad():
        for e in conjunto:
            if all(operacion(e, a) == a and operacion(a, e) == a for a in conjunto):
                print(f"El elemento neutro es {e}")
                return e
            return None

    def inversos(identidad):
        inv = {}
        for a in conjunto:
            ind = False #Indicador para veri si algun elemento no tiene inverso
            for b in conjunto:
                if (operacion(a, b) == identidad and operacion(b, a) == identidad) == True:
                    inv[a] = b
                    ind = True
        if ind == True:
            print(f"Los inversos de cada elemento son los siguientes: {inv}")
            return True
        else:
            return False

    # Verificar las propiedades del grupo
    if not cerradura():
        print("No es un grupo: la cerradura no se cumple")
        return False
    if not asociatividad():
        print("No es un grupo: la asociatividad no se cumple")
        return False
    identidad = encontrar_identidad()
    if identidad is None:
        print("No es un grupo: no se encontró el elemento identidad")
        return False
    if not inversos(identidad):
        print("No es un grupo: no todos los elementos tienen inversos")
        return False
    return True


def es_grupo_ciclico(conjunto, operacion):
    for g in conjunto:
        generado = set(operacion(g, i) for i in range(len(conjunto)))
        if generado == set(conjunto):
            print("Es un grupo cíclico")
            return True

    print("No es un grupo cíclico")
    return False

def encontrar_subgrupos(conjunto, operacion):
    def generar_subgrupo(g):
        subgrupo = set()
        elemento = g
        while elemento not in subgrupo:
            subgrupo.add(elemento)
            elemento = operacion(elemento, g)
        return subgrupo

    subgrupos = []
    elementos_vistos = set()

    for g in conjunto:
        if g not in elementos_vistos:
            subgrupo = generar_subgrupo(g)
            subgrupos.append(subgrupo)
            elementos_vistos.update(subgrupo)

    return subgrupos

def encontrar_todos_los_subgrupos(conjunto, operacion):
    subgrupos = []

    def generar_subgrupo(g):
        subgrupo = set()
        elemento = g
        while elemento not in subgrupo:
            subgrupo.add(elemento)
            elemento = operacion(elemento, g)
        return subgrupo

    for g in conjunto:
        subgrupo = generar_subgrupo(g)
        subgrupos.append(subgrupo)

    return np.unique(subgrupos)


# Ejemplo de uso
conjunto = {0, 1, 2, 3, 4, 5}
n = 6
operacion = lambda a, b: (a + b) % n

if es_grupo(conjunto, operacion) == True:
    print("El conjunto con la operacion es un grupo")
    es_grupo_ciclico(conjunto, operacion)
    print(f"Los subgrupos generados son los siguientes: {encontrar_todos_los_subgrupos(conjunto, operacion)}")

