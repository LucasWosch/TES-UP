# Verificador de Aprovação

nota = float(input("Digite a nota do aluno: "))
frequencia = float(input("Digite a frequência (%): "))

if nota >= 6.0 and frequencia >= 75:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado.")