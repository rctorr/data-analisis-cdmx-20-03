# 1. lee el valor desde usuario
# 2. El valor es un entero?
# 3. Si es entero, imprimirlo y terminar
# 4. Si no es entero imprimir mensaje de error y ejecutar 1.
es_entero = False
while not es_entero:  # False -> not False -> True
    valor = input("Dame un entero humano:")
    if valor.isdigit():
        n = int(valor)
        print(n)
        print(type(n))
        es_entero = True
    else:
        print("Error: el valor proporcionado no es un entero!")
        print("---")
