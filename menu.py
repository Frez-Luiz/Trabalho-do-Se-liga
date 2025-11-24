import random

print ("_____________________________________\n")
print ("//         Luiz Felipe            //")
print ("///   Bem vindo ao meu jogo      ///")
print ("_____________________________________")

def menu_principal():
    print("     Qual você quer utilizar?  ")
    print(" (1)- Calcular Idade (2)- Calcular Compra (3)- Sair")
    opcao = input("Escolha uma opção (1, 2 ou 3): ")
    if opcao == '1':
            calcular_idade()
    elif opcao == '2':
            calcular_preco_compra()
    elif opcao == '3':
            print("Saindo do programa. Obrigado!")
            break
 

def calcular_idade():
nome = input("Digite seu nome: ")
print ("Bem-vindo, " + nome + "!")

idade = int(input("Digite sua idade: "))
print (f"No próximo ano você terá {idade + 1} anos." )


