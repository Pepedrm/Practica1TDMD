'''
    Un subconjunto A es dirigido bajo una relación de orden parcial R si para cada par de elementos 
    a,b ∈ A. Existe un elemento c ∈ A tal que (a,c)∈R y (b,c)∈R.  
    Es decir, todo par de elementos en A tiene un "mayor común superior" en A.
'''

def es_dirigido(P, R, A):
    """Verifica si el subconjunto A es dirigido bajo la relación R."""
    # Para cada par de elementos (a, b) en A
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            a, b = A[i], A[j]
            encontrado_mayor_comun_superior = False
            # Verificamos si existe un c en A tal que (a, c) y (b, c) pertenezcan a R
            for c in A:
                if (a, c) in R and (b, c) in R:
                    encontrado_mayor_comun_superior = True
                    break
            # Si no se encontró tal c, entonces A no es dirigido
            if not encontrado_mayor_comun_superior:
                return False
    # Si se cumple para todos los pares, A es dirigido
    return True
def main():
    # Ejemplo de uso

    # Conjunto P de elementos
    P = [1, 2, 3, 4, 5]

    # Relación de orden parcial R (representada como un conjunto de pares ordenados)
    R1 = {(1, 1), (2, 2), (3, 3), (4, 4), (5, 5),
        (1, 2), (1, 3), (2, 4), (3, 5), (4, 5)}
    
    R2 = {(1, 1), (2, 2), (3, 3), (4, 4), (5, 5),
         (1, 2), (1, 3), (2,3), (2, 4), (3, 5), (4, 5)}

    # Subconjunto A de P
    A = [1, 2, 3]

    # Verificar si A es dirigido
    if es_dirigido(P, R2, A):
        print("El subconjunto A es dirigido.")
    else:
        print("El subconjunto A no es dirigido.")

if __name__ == "__main__":
    main()