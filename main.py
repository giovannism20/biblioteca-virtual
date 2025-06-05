from view.menu_biblioteca import menu_biblioteca
from view.menu_busca_livro import menu_busca_livro
from view.menu_altera_dados_livro import menu_altera_dados_livro

from controller.biblioteca_controller import (
    cadastrar_biblioteca,
    alterar_nome_biblioteca,
    excluir_biblioteca,
    listar_bibliotecas_cadastradas
)

from controller.livro_controller import (
    cadastrar_livro,
    alterar_livro,
    excluir_livro,
    listar_livros_cadastrados,
    pesquisar_livro
)

from controller.vinculo_livro_biblioteca_controller import (
    adicionar_livro_biblioteca,
    remover_livro_biblioteca,
    listar_livro_biblioteca,
    status_livro_biblioteca
)

from controller.sair_controller import sair


if __name__ == "__main__":
    while True:
        menu_biblioteca()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_biblioteca()
        elif opcao == "2": 
            alterar_nome_biblioteca()
        elif opcao == "3":
            excluir_biblioteca()
        elif opcao == "4":
            listar_bibliotecas_cadastradas()
        elif opcao == "5":
            cadastrar_livro()
        elif opcao == "6":
            alterar_livro()
        elif opcao == "7":
            excluir_livro()
        elif opcao == "8":
            listar_livros_cadastrados()
        elif opcao == "9":
            adicionar_livro_biblioteca()
        elif opcao == "10":
            remover_livro_biblioteca()
        elif opcao == "11":
            listar_livro_biblioteca()
        elif opcao == "12":
            status_livro_biblioteca()
        elif opcao == "13":
            pesquisar_livro()
        elif opcao == "14":
            sair()
