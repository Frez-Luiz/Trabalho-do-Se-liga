
print("     Qual você quer utilizar?  ")
print(" (1)- Calcular Idade (2)- Calcular Compra (3)- Sair")




print ("_____________________________________\n")
print ("//         Luiz Felipe            //")
print ("///   Bem vindo ao meu jogo      ///")
print ("_____________________________________")


def calcular_idade():
       nome = input("Digite seu nome: ")
       print ("Bem-vindo, " + nome + "!")
       idade = int(input("Digite sua idade: "))
       print (f"No próximo ano você terá {idade + 1} anos." )
