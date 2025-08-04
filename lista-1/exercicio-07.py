# Gerador de Tabuada Personalizada

numero = int(input("Digite o número para gerar a tabuada: "))
limite = int(input("Até qual número deseja a tabuada? "))

print(f"\nTabuada do {numero} até {limite}:\n")

for i in range(1, limite + 1):
    print(f"{numero} x {i} = {numero * i}")