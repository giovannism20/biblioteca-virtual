from view.mensagens import mostrar_mensagem
from view.menu_biblioteca import menu_biblioteca

from controller.biblioteca import (
    cadastrar_biblioteca,
    alterar_nome_biblioteca,
    excluir_biblioteca,
    listar_bibliotecas_cadastradas
)

from controller.livro import (
    cadastrar_livro,
    alterar_livro,
    excluir_livro,
    listar_livros_cadastrados,
    pesquisar_livro
)

from controller.vinculo_livro_biblioteca import (
    adicionar_livro_biblioteca,
    remover_livro_biblioteca,
    listar_livro_biblioteca,
    status_livro_biblioteca
)

if __name__ == "__main__":
    while True:
        menu_biblioteca()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            MENSAGEM = cadastrar_biblioteca()
            mostrar_mensagem(MENSAGEM)
        elif opcao == "2":
            MENSAGEM = alterar_nome_biblioteca()
            mostrar_mensagem(MENSAGEM)
        elif opcao == "3":
            MENSAGEM = excluir_biblioteca()
            mostrar_mensagem(MENSAGEM)
        elif opcao == "4":
            MENSAGEM = listar_bibliotecas_cadastradas()
        elif opcao == "5":
            MENSAGEM = cadastrar_livro()
            mostrar_mensagem(MENSAGEM)
        elif opcao == "6":
            MENSAGEM = alterar_livro()
            mostrar_mensagem(MENSAGEM)
        elif opcao == "7":
            MENSAGEM = excluir_livro()
            mostrar_mensagem(MENSAGEM)
        elif opcao == "8":
            MENSAGEM = listar_livros_cadastrados()
        elif opcao == "9":
            MENSAGEM = adicionar_livro_biblioteca()
            mostrar_mensagem(MENSAGEM)
        elif opcao == "10":
            MENSAGEM = remover_livro_biblioteca()
            mostrar_mensagem(MENSAGEM)
        elif opcao == "11":
            MENSAGEM = listar_livro_biblioteca()
            mostrar_mensagem(MENSAGEM)
        elif opcao == "12":
            MENSAGEM = status_livro_biblioteca()
            mostrar_mensagem(MENSAGEM)
        elif opcao == "13":
            MENSAGEM = pesquisar_livro()
            mostrar_mensagem(MENSAGEM)
        elif opcao == "14":
            print("Saindo... Até a próxima!")
            break
