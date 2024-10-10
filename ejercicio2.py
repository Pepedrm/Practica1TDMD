"Utilizo las 4 funciones del ejercicio anterior para hacer el ejercicio 2"

def es_reflexiva(P, R):
    """Verifica si la relación es reflexiva."""
    for a in P:
        if (a, a) not in R:
            return False
    return True

def es_antisimetrica(P, R):
    """Verifica si la relación es antisimétrica."""
    for a, b in R:
        if a != b and (b, a) in R:
            return False
    return True

def es_transitiva(P, R):
    """Verifica si la relación es transitiva."""
    for a, b in R:
        for c, d in R:
            if b == c and (a, d) not in R:
                return False
    return True

def es_orden_parcial(P, R):
    """Verifica si la relación es un orden parcial."""
    return es_reflexiva(P, R) and es_antisimetrica(P, R) and es_transitiva(P, R)

def generar_pares(P):
    """Genera todos los pares posibles de elementos en el conjunto P."""
    pares = []
    for a in P:
        for b in P:
            pares.append((a, b))
    return pares

def generar_relaciones(P):
    """Genera todas las relaciones posibles en el conjunto P."""
    pares = generar_pares(P)  # Todos los pares posibles
    n = len(pares)
    todas_las_relaciones = []
    
    for i in range(2**n):
        relacion = set()
        for j in range(n):
            if (i >> j) & 1:  # Verifica si el bit j está encendido
                relacion.add(pares[j])
        todas_las_relaciones.append(relacion)
    
    return todas_las_relaciones

def encontrar_ordenes_parciales(P):
    """Encuentra todas las relaciones que son órdenes parciales."""
    relaciones_posibles = generar_relaciones(P)
    ordenes_parciales = [R for R in relaciones_posibles if es_orden_parcial(P, R)]
    return ordenes_parciales


def main():
    # Ejemplo con conjunto de 3 elementos
    # P3 = [1, 2, 3]
    # ordenes_parciales_3 = encontrar_ordenes_parciales(P3)
    # print(f"Órdenes parciales con 3 elementos: {len(ordenes_parciales_3)}")
    # for i, orden in enumerate(ordenes_parciales_3, 1):
    #     print(f"Orden parcial {i}: {orden}")

    # Ejemplo con conjunto de 4 elementos
    P4 = [1, 2, 3, 4]
    ordenes_parciales_4 = encontrar_ordenes_parciales(P4)
    print(f"\nÓrdenes parciales con 4 elementos: {len(ordenes_parciales_4)}")
    for i, orden in enumerate(ordenes_parciales_4, 1):
        print(f"Orden parcial {i}: {orden}")


if __name__ == "__main__":
    main()