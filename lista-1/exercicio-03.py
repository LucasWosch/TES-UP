# Calculadora Simples

num1 = float(input(f"Digite o número 1: "))
num2 = float(input(f"Digite o número 2: "))

soma            = num1 + num2
subtracao       = num1 - num2
multiplicacao   = num1 * num2
divisao         = num1 / num2 if 0 not in [num1,num2] else "Não é possível realizar divisão por 0"

print(f"Resultado da soma ({num1} + {num2}): {soma}")
print(f"Resultado da subtracao ({num1} - {num2}): {subtracao}")
print(f"Resultado da multiplicacao ({num1} * {num2}): {multiplicacao}")
print(f"Resultado da divisao ({num1} / {num2}): {divisao}")
