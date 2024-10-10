def es_orden_parcial(P, R):
    """
    Una relación es un orden parcial si es reflexiva, antisimétrica y transitiva.
        - Será reflexiva si cada par de elementos de P se encuentra en R.
        - Será antisimétrica si para cada par de elementos a y b con a!=b, (b, a) no se encuentra en R.
        - Será transitiva si para cualquier trio de elementos a, b y c. Si a está relacionado con b, y b con c, 
                entonces a con c debe también estarlo
    """
    return es_reflexiva(P, R) and es_antisimetrica(P, R) and es_transitiva(P, R)

def es_reflexiva(P, R):
    for a in P:
        if (a, a) not in R:
            return False
    return True

def es_antisimetrica(P, R):
    for a, b in R:
        if a != b and (b, a) in R:
            return False
    return True

def es_transitiva(P, R):
    for a, b in R:
        for c, d in R:
            if b == c and (a, d) not in R:
                return False
    return True



# Ejemplo de uso
P = {1, 2, 3}
R1 = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 3)}
R2 = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 3), (1,3)}

print("============================================")
if es_orden_parcial(P, R2):
    print("La función es un orden parcial.")
else:
    print("La relación no es un orden parcial.")
print("============================================")