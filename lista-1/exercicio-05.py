# Classificação de Idade

idade = int(input("Digite a idade do usuário: "))

if idade <= 12:
    classificacao = "Criança"
elif idade <= 17:
    classificacao = "Adolescente"
elif idade <= 59:
    classificacao = "Adulto"
else:
    classificacao = "Idoso"

print(f"Usuário possui {idade} e foi classificado como: {classificacao}")

