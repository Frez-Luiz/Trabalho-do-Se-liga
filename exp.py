import random

def calcular_idade():
    nome = input("Digite seu nome: ")
    print ("Bem-vindo, " + nome + "!")
    idade = int(input("Digite sua idade: "))
    print (f"No próximo ano você terá {idade + 1} anos." )

def calcular_compra():
    total = 0
    while True:
        try:
            preco_item = float(input("Digite o preço do item (ou 0 para finalizar): R$ "))
            if preco_item == 0:
                break
            total += preco_item
        except ValueError:
            print("Preço inválido. Tente novamente.")
    print(f"\nO preço total da compra é de R$ {total:.2f}.\n")

def menu_principal():
    while True:
        print ("__________________________________________\n")
        print ("////////////////////////////////////////////")
        print ("////           Luiz Felipe              ////")
        print ("//////   Bem vindo ao meu programa!   //////")
        print ("////////////////////////////////////////////")
        print ("____________________________________________")

        print("     Qual você quer utilizar?  ")
        print(" (1)- Calcular Idade (2)- Calcular Compra (3)- Sair")


        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            calcular_idade()
        elif opcao == '2':
            calcular_compra()
        elif opcao == '3':
            print("Você saiu do programa!")
            break
        else:
            print("Opção inválida. Por favor, escolha as opções presentes no programa!")

if __name__ == "__main__":
    menu_principal()
