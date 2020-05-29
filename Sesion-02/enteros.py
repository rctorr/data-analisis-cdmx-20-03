# 1. Leer N como dato proporcionado por el usuario
es_entero = False
while not es_entero:  # False -> not False -> True
    valor = input("Dame un entero humano:")
    if valor.isdigit():
        n = int(valor)
        es_entero = True
    else:
        print("Error: el valor proporcionado no es un entero!")
        print("---")

# 2. Crear la lista de enteros
enteros = []
for i in range(n):
s    enteros.append(i)  # enteros = [0, 1, 2, ..., n]

# 3. Imprimir la lista de enteros
for valor in enteros:
    print(valor)
