vetor = [6, 5, 76, 9, 4, 5, 7, 8]
menor = vetor[0]

for i in range(len(vetor)):
  if vetor[i] < menor:
    menor = vetor[i]

print(menor)
