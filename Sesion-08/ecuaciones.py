import numpy as np

# a x = b

# Definición de constantes
a = np.array(
        (
            [2, 1, -3],
            [5, -4, 1],
            [1, -1, -4]
        )
    )

b = np.array( [7, -19, 4] )

# Encontrando la solución al sistema
x = np.linalg.solve(a, b)

# Imprimiendo resultados
print("x =", x)

# comprobando solución: a x -> b
bp = np.dot(a, x)
print("bp=", bp)
