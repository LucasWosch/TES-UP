# Cálculo de Média e Aprovação

qtdAlunos   = 1
qtdNotas    = 2
alunos      = []

for numAluno in range(0, qtdAlunos):
    nome    = input(f"Digite o nome do aluno {numAluno + 1}: ")
    notas   = []
    for numNota in range(0, qtdNotas):
        notas.append(float(input(f"Digite a nota {numNota + 1}: ")))
    media   = sum(notas) / qtdNotas
    status  = "aprovado" if media >= 6 else "reprovado"
    alunos.append({"nome": nome, "notas": notas, "media": media, "status": status})
    print(f"Aluno {numAluno + 1} {status} com uma média de: {media}")

# print(alunos)


