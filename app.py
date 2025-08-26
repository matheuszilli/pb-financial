def _menu_principal():
    """
    Exibe o menu principal com todas as opções disponíveis.
    """
    print("\n=== Menu Principal ===")
    print("1. Visualizar Carteira")
    print("2. Comprar Ação")
    print("3. Vender Ação")
    print("4. Definir Meta")
    print("0. Sair")

def _acoes_menu():
    """
    Função principal que executa o loop do programa.
    
    Controla o fluxo principal da aplicação, apresentando o menu
    e executando as funções baseadas na escolha do usuário.
    """
    while True:
        _menu_principal()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            from carteira import _exibir_carteira
            _exibir_carteira()
        elif opcao == "2":
            from carteira import comprar_acao
            comprar_acao(None)
        elif opcao == "3":
            from carteira import vender_acao
            vender_acao()
        elif opcao == "4":
            from carteira import definir_meta
            definir_meta()
        elif opcao == "0":
            print("\nSaindo do programa...")
            break
        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    _acoes_menu()