vetor = []
pergunta = int(input("Digite numero: "))

while pergunta > 0:
    vetor.append(pergunta)
    pergunta = int(input("Digite numero: "))

for i in range(len(vetor)):
    print(vetor[i])