# [PY-A07]Você foi contratado para desenvolver um programa que calcule a média de notas dos alunos de uma turma.
# Para isso, você deverá criar uma lista com as notas de cada aluno e, em seguida, implementar uma função que calcule a média aritmética das notas.
# Além disso, você deverá utilizar um loop while para pedir ao usuário que insira as notas dos alunos até que ele decida parar.
# Por fim, você deverá utilizar um loop for para imprimir a média de cada aluno.

# a) Escreva o código para a função que calcule a média aritmética das notas.

notas_geral = []
notas = []
nota_aluno = 0.00

def media(x = 0):
    for notas in notas_geral:
        x = 0
        for nota in notas:
            x += nota
        print(f"A média total das notas foi de: {x/len(notas)}")

# b) Escreva o código para o loop while que pede ao usuário que insira as notas dos alunos.

while True:
    nota_aluno = float(input("Insira a nota do aluno, para finalizar digite uma nota negativa: "))
    if nota_aluno >= 0:
        notas.append(nota_aluno)
    else:
        if input("Você deseja inserir notas de um novo aluno (S/N)? ") == "N":
            notas_geral.append([nota for nota in notas])
            print(notas_geral)
            break
        else:
            notas_geral.append([nota for nota in notas])
            notas.clear()

# c) Escreva o código para o loop for que imprime a média de cada aluno.

media()