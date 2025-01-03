# Inicializando o tabuleiro como uma matriz 3x3 vazia
tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

# Função para exibir o tabuleiro
def exibir_tabuleiro():
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 5)

# Função principal do jogo
def jogo_da_velha():
    jogador_atual = "X"
    jogadas = 0

    while jogadas < 9:  # O jogo termina após 9 jogadas (3x3)
        exibir_tabuleiro()
        print(f"Jogador {jogador_atual}, é a sua vez.")

        # Pegar a linha e coluna da jogada
        linha = int(input("Digite a linha (0, 1 ou 2): "))
        coluna = int(input("Digite a coluna (0, 1 ou 2): "))

        # Verificar se a posição está vazia
        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual  # Faz a jogada
            jogadas += 1  # Conta mais uma jogada

            # Alternar jogador
            jogador_atual = "O" if jogador_atual == "X" else "X"
        else:
            print("Posição ocupada! Tente novamente.")

    exibir_tabuleiro()
    print("Fim do jogo!")

# Executar o jogo
jogo_da_velha()
