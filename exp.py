import datetime

def calcular_idade():
    """Função para calcular a idade com base no ano de nascimento."""
    try:
        ano_nascimento = int(input("Digite o ano de nascimento (YYYY): "))
        ano_atual = datetime.date.today().year
        idade = ano_atual - ano_nascimento
        print(f"\nSua idade é de aproximadamente {idade} anos.\n")
    except ValueError:
        print("\nEntrada inválida. Por favor, digite um ano válido.\n")

def calcular_preco_compra():
    """Função para calcular o preço total de uma compra."""
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
    """Função principal que exibe o menu e gerencia as opções."""
    while True:
        print("="*30)
        print(" MINI-PROGRAMA COM MENU")
        print("="*30)
        print("1 - Calcular idade")
        print("2 - Calcular preço da compra")
        print("3 - Sair")
        print("="*30)

        opcao = input("Escolha uma opção (1, 2 ou 3): ")

        if opcao == '1':
            calcular_idade()
        elif opcao == '2':
            calcular_preco_compra()
        elif opcao == '3':
            print("Saindo do programa. Obrigado!")
            break
        else:
            print("\nOpção inválida. Por favor, escolha 1, 2 ou 3.\n")

# Garante que o menu principal seja executado quando o script iniciar
if __name__ == "__main__":
    menu_principal()