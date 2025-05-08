""""2. Implemente o programa que leia a nota de vários alunos de uma turma e gere uma tela de saída
com as seguintes informações: a quantidade de alunos aprovados, a quantidade de alunos
reprovados e a quantidade de alunos que fizeram a prova. Considere que o aluno será aprovado com
nota for maior ou igual a cinco. """

contador_aprovados = 0
contador_reprovados = 0
contador_alunos = 0
print("Digite (0) para parar de digitar as notas.")
while True:
    nota = float(input("Digite a nota do(a) aluno(a): "))
    if nota == 0:
        break
    if nota >= 5:
        contador_aprovados = contador_aprovados + 1
    else:
        contador_reprovados = contador_reprovados + 1
    contador_alunos = contador_alunos + 1
print(f"A quantidade de alunos aprovados é: {contador_aprovados}.")
print(f"A quantidade de alunos reprovados é: {contador_reprovados}.")
print(f"A quantidade de alunos que fizeram a prova é: {contador_alunos}.")