# Simulação de Compras

total = 0
for i in range(1, 4):
    nome = input(f"Digite o nome do produto {i}: ")
    preco = float(input(f"Digite o preço de {nome}: R$ "))
    total += preco

if total > 100:
    total *= 0.9  # aplica 10% de desconto

print(f"\nValor total com desconto (se aplicável): R$ {round(total, 2)}")