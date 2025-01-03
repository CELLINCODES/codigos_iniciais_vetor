senha_correta = "12345"
tentativas = 3

while tentativas > 0: #cria um loop para as tentativas
    senha = input("Digite sua senha: ")

    if senha == senha_correta:
        print("Foi")
        break #quebra de loop

    else: 
        tentativas -=1
        print("tem poucas chances ainda ")

    if tentativas == 0:
        print("block")