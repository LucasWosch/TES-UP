# IMC

altura  = int(input("Digite a altura do usuário (cm): "))
peso    = float(input("Digite o peso do usuário (kg): "))

alturaM = round(altura / 100, 2)
imc     = round(peso / (alturaM * alturaM),2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

print(f"O usuário com um IMC de {imc} sendo classificado como: {classificacao}")

