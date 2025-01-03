# Criando uma matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Acessando elementos
print(matriz[0][0])  # Saída: 1 (primeira linha, primeira coluna)
print(matriz[1][2])  # Saída: 6 (segunda linha, terceira coluna)

# Alterando um elemento
matriz[2][1] = 10  # Mudando o 8 para 10
print(matriz)  # Saída: [[1, 2, 3], [4, 5, 6], [7, 10, 9]]
