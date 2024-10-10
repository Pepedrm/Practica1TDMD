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

def es_dirigido(P, R, A):
    """Verifica si el subconjunto A es dirigido bajo la relación R."""
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            a, b = A[i], A[j]
            encontrado_mayor_comun_superior = False
            for c in A:
                if (a, c) in R and (b, c) in R:
                    encontrado_mayor_comun_superior = True
                    break
            if not encontrado_mayor_comun_superior:
                return False
    return True

def encontrar_supremo(P, R, A):
    """Encuentra el supremo de un subconjunto dirigido A bajo la relación R."""
    posibles_supremos = []
    for c in P:
        if all((a, c) in R for a in A):
            posibles_supremos.append(c)
    
    if not posibles_supremos:
        return None
    
    supremo = posibles_supremos[0]
    for s in posibles_supremos:
        if (s, supremo) in R and s != supremo:
            supremo = s
    return supremo

def es_dcpo(P, R):
    """Verifica si P es un dcpo bajo la relación R."""
    # Verificar si es un orden parcial
    if not es_orden_parcial(P, R):
        return False
    
    # Verificar que cada subconjunto dirigido tiene un supremo
    for tamano_subconjunto in range(2, len(P) + 1):
        subconjuntos_dirigidos = []
        
        # Generar todos los subconjuntos dirigidos de tamaño tamano_subconjunto
        for i in range(len(P)):
            A = P[i:i+tamano_subconjunto]
            if len(A) == tamano_subconjunto and es_dirigido(P, R, A):
                subconjuntos_dirigidos.append(A)
        
        # Verificar que cada subconjunto dirigido tiene un supremo
        for A in subconjuntos_dirigidos:
            if encontrar_supremo(P, R, A) is None:
                return False
    
    return True
def main():
    # Ejemplo de uso

    # Conjunto P de elementos
    P1 = [1, 2, 3, 4, 5]

    # Relación de orden parcial R (representada como un conjunto de pares ordenados)
    R1 = {(1, 1), (2, 2), (3, 3), (4, 4), (5, 5),
        (1, 2), (1, 3), (2, 4), (3, 5), (4, 5)}
    
    P2 = [1,2,3]

    R2 = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 3), (1, 3)}

    # Verificar si P es un dcpo bajo la relación R
    if es_dcpo(P2, R2):
        print("El conjunto P es un dcpo.")
    else:
        print("El conjunto P no es un dcpo.")

if __name__ == "__main__":
    main()