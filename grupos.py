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

def seleccionar_operacion():
    print("Seleccione la operación:")
    print("1. Suma módulo n")
    print("2. Resta módulo n")
    print("3. Multiplicación")
    print("4. Operación personalizada")

    opcion = int(input("Ingrese el número de la operación deseada: "))

    if opcion == 1:
        n = int(input("Ingrese el valor de n para la suma módulo n: "))
        return lambda a, b: (a + b) % n
    elif opcion == 2:
        n = int(input("Ingrese el valor de n para la resta módulo n: "))
        return lambda a, b: (a - b) % n
    elif opcion == 3:
        return lambda a, b: a * b
    elif opcion == 4:
        return definir_operacion_personalizada(conjunto)
    else:
        print("Opción no válida")
        return None

def definir_operacion_personalizada(conjunto):
    print("Defina la tabla de Cayley:")
    elementos = sorted(conjunto)
    n = len(elementos)
    tabla = []
    for i in range(n):
        fila = input(f"Ingrese la fila {elementos[i]} de la tabla de Cayley, separados por comas: ").split(",")
        if len(fila) != n:
            print("La cantidad de elementos en la fila no coincide con la cantidad de elementos en el conjunto.")
            return None
        tabla.append(fila)

    def operacion(a, b):
        return tabla[elementos.index(a)][elementos.index(b)]

    return operacion

# Ejemplo de uso
conjunto = input("Ingrese los elementos del conjunto separados por comas: ").split(",")
operacion = seleccionar_operacion()

if operacion:
    tabla_cayley = generar_tabla_cayley(conjunto, operacion)
    print("Tabla de Cayley:")
    print(tabla_cayley)

    if es_grupo(conjunto, operacion):
        print("El conjunto con la operación es un grupo")
        es_grupo_ciclico(conjunto, operacion)
    else:
        print("El conjunto con la operación no es un grupo")

    subgrupos = encontrar_todos_los_subgrupos(conjunto, operacion)
    print(f"Subgrupos encontrados: {subgrupos}")

else:
    print("No se seleccionó una operación válida.")
# Ejemplo de uso
if es_grupo(conjunto, operacion) == True:
    print("El conjunto con la operacion es un grupo")
    es_grupo_ciclico(conjunto, operacion)
    print(f"Los subgrupos generados son los siguientes: {encontrar_todos_los_subgrupos(conjunto, operacion)}")

