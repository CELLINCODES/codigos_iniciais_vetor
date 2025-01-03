nota = [

    [6.0, 7.5, 8.0],
    [6.5, 5.5, 9.0],
    [7.0, 7.0, 4.5]
]

for i in range(len(nota)): #percorre tudo
    aluno_nota = nota[i]
    soma = 0.0

    for n in aluno_nota:
        soma += n

    media = soma / len(aluno_nota)

    print(f"Aluno {i + 1} - Notas: {aluno_nota} - Média: {media:.2f}")