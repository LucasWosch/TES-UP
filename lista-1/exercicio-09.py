# Verificador de Palíndromos

texto = input("Digite uma palavra ou frase: ").lower().replace(" ", "").replace(".", "").replace(",", "")
inverso = texto[::-1]

if texto == inverso:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")