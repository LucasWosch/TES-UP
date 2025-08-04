# Análise de Notas de Turma

qtd_alunos = int(input("Digite a quantidade de alunos: "))
notas = []

for i in range(qtd_alunos):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    notas.append(nota)

media_geral = sum(notas) / qtd_alunos
maior_nota = max(notas)
menor_nota = min(notas)

print(f"\nMédia geral da turma: {media_geral:.2f}")
print(f"Maior nota: {maior_nota}")
print(f"Menor nota: {menor_nota}")