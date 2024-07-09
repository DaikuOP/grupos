from grupos import group

conjunto = input("Ingrese los elementos del conjunto separados por comas: ").split(",")
conjunto = list(map(int, conjunto))
operacion = group.seleccionar_operacion()

if operacion:
    tabla_cayley = group.generar_tabla_cayley(conjunto, operacion)
    print("Tabla de Cayley:")
    print(tabla_cayley)

    if group.es_grupo(conjunto, operacion) == True:
        print("El conjunto con la operación es un grupo")
        group.es_grupo_ciclico(conjunto, operacion)
    else:
        print("El conjunto con la operación no es un grupo")

    subgrupos = group.encontrar_todos_los_subgrupos(conjunto, operacion)
    print(f"Subgrupos encontrados: {subgrupos}")

else:
    print("No se seleccionó una operación válida.")

