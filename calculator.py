def soma (x, y):
    return x + y
def subtração(x, y):
    return x - y
def multiplicação(x, y):
    return x * y
def divisão(x, y):
    if y == 0:
        return None
        print("sem valor")
    return x / y

def calculadora():
    print("selecione")
    print("1- Soma")
    print("2- Subtração")    
    print("3- Multiplicação")
    print("4- Divisão")

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))

escolha = input("escolha uma opção 1/2/3/4: ")

if escolha == "1":
    print("O valor será", soma (n1, n2))
elif escolha == "2":
    print("o valor será", subtração (n1, n2))
elif escolha == "3":
    print("o valor será", multiplicaçãoo (n1, n2))
elif escolha == "4":
    print("o valor será", divisão (n1, n2))
else:
    print("sem valor")


calculadora()