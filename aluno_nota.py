alunos = []
notas = []

for i in range(5):
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    nota = float(input(f"Digite a nota do {i+1}º aluno: "))
    
    alunos.append(nome)
    notas.append(nota)

print("\nDados dos alunos: ")
for i in range(5):
    print(f"Nome: {alunos[i]} - Nota: {notas[i]}")