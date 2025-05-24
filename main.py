from model import *
from view.menu_biblioteca import menu_biblioteca
import util

if __name__ == "__main__":
    while True:
        menu_biblioteca()
        opcao = input("Escolha uma opção: ")
        util.limpar_tela()

        if opcao == "1":
            biblioteca.cadastrar_livro()
        elif opcao == "2":
            biblioteca.listar_livros()
        elif opcao == "3":
            biblioteca.alterar_status()
        elif opcao == "4":
            biblioteca.buscar_livros()
        elif opcao == "5":
            biblioteca.exportar_lista()
        elif opcao == "6":
            print("Saindo...  Até a próxima!")
            break
        else:
            print("Opção inválida. Tente novamente.")
