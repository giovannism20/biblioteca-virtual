from view.mensagens import mostrar_mensagem
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

if __name__ == "__main__":
    while True:
        menu_biblioteca()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mensagem = cadastrar_biblioteca()
            mostrar_mensagem(mensagem)
        elif opcao == "2":
            mensagem = alterar_nome_biblioteca()
            mostrar_mensagem(mensagem)
        elif opcao == "3":
            mensagem = excluir_biblioteca()
            mostrar_mensagem(mensagem)
        elif opcao == "4":
            mensagem = listar_bibliotecas_cadastradas()
        elif opcao == "5":
            mensagem = cadastrar_livro()
            mostrar_mensagem(mensagem)
        elif opcao == "6":
            mensagem = alterar_livro()
            mostrar_mensagem(mensagem)
        elif opcao == "7":
            mensagem = excluir_livro()
            mostrar_mensagem(mensagem)
        elif opcao == "8":
            mensagem = listar_livros_cadastrados()
        elif opcao == "9":
            mensagem = adicionar_livro_biblioteca()
            mostrar_mensagem(mensagem)
        elif opcao == "10":
            mensagem = remover_livro_biblioteca()
            mostrar_mensagem(mensagem)
        elif opcao == "11":
            mensagem = listar_livro_biblioteca()
            mostrar_mensagem(mensagem)
        elif opcao == "12":
            mensagem = status_livro_biblioteca()
            mostrar_mensagem(mensagem)
        elif opcao == "13":
            mensagem = pesquisar_livro()
            mostrar_mensagem(mensagem)
        elif opcao == "14":
            print("Saindo... Até a próxima!")
            break
