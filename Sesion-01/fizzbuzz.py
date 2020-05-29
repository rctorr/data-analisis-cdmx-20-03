# 1. Imprimir lista de números de 1 al 20
# 2. Remplazar los múltiplos de 3 por Fizz
# 3. Remplazar los múltiplos de 5 por Buzz
# 4. Remplazar los múltiplos de 3 y 5 por FizzBuzz
n = 20
for i in range(1, n+1):  # 1, , 2, ... n
    if i % 3 == 0:  # i es múltiplo de 3
        if i % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")        
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
