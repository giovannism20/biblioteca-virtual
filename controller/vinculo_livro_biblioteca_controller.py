from model.biblioteca import Biblioteca
from model.livro import Livro

from util import exibir_lista_bibliotecas, exibir_lista_livros, buscar_livros, exibir_lista_nomeada
from view.menu_biblioteca import menu_biblioteca
from view.menu_busca_livro import menu_busca_livro
from view.menu_altera_dados_livro import menu_altera_dados_livro
from data_store import bibliotecas, livros


def adicionar_livro_biblioteca():
    if not bibliotecas:
        print("Ainda não há bibliotecas cadastradas.")
        return

    lista_bibliotecas = exibir_lista_nomeada(bibliotecas)

    if not lista_bibliotecas:
        return

    escolha_biblioteca = input(
        "Digite o número da biblioteca ou 0 para cancelar: "
    )

    if escolha_biblioteca == "0":
        print("Ação cancelada.")
        return

    if escolha_biblioteca.isdigit():
        index = int(escolha_biblioteca)

        if index in lista_bibliotecas:
            nome_selecionado = lista_bibliotecas[index]
            instancia_biblioteca = bibliotecas[nome_selecionado]

            if not livros:
                print("Ainda não há livros cadastrados.")
                return

            lista_livros = exibir_lista_nomeada(livros)

            if not lista_livros:
                return

            escolha_livro = input("Digite o número do livro: ")

            if escolha_livro.isdigit():
                index = int(escolha_livro)

                if index in lista_livros:
                    nome_selecionado = lista_livros[index]
                    instancia_livro = livros[nome_selecionado]

                    instancia_biblioteca.cadastrar_livro(instancia_livro)
                    instancia_biblioteca.listar_livros()
                else:
                    print("Número inválido.")
            else:
                print("Número inválido.")
        else:
            print("Número inválido.")
    else:
        print("Entrada inválida. Digite um número válido.")

def remover_livro_biblioteca():
    lista_bibliotecas = exibir_lista_bibliotecas(bibliotecas)
    if not lista_bibliotecas:
        print("Ainda não há bibliotecas cadastradas.")
        return

    escolha_biblioteca = input(
        "Digite o número da biblioteca"
        "ou 0 para cancelar: ")

    if escolha_biblioteca == "0":
        print("Ação cancelada.")
        return

    if not escolha_biblioteca.isdigit():
        print("Entrada inválida.")
        return

    index = int(escolha_biblioteca)
    if not index in lista_bibliotecas:
        print("Número inválido.")
        return

    nome_biblioteca = lista_bibliotecas[index]
    biblioteca = bibliotecas[nome_biblioteca]

    if not biblioteca.livros:
        print(f"A biblioteca '{nome_biblioteca}' não possui livros cadastrados.")
        return

    print(f"\nLivros da biblioteca '{nome_biblioteca}':")
    for index, registro in enumerate(biblioteca.livros, start=1):
        print(f"{index} - {registro['livro'].titulo}")

    escolha_livro = input("Digite o número do livro que deseja remover: ")
    if not escolha_livro.isdigit():
        print("Entrada inválida.")
        return

    index_livro = int(escolha_livro)
    if index_livro < 1 or index_livro > len(biblioteca.livros):
        print("Número inválido.")
        return

    livro_remover = biblioteca.livros[index_livro - 1]["livro"]

    confirmacao = (
        input(
        f"Tem certeza que deseja remover '{livro_remover.titulo}' "
        f"da biblioteca '{nome_biblioteca}'? (s/n): "
        )
    .strip()
    .lower()
    )
    if confirmacao == "s":
        biblioteca.remover_livro(livro_remover)
    else:
        print(" Remoção cancelada.")

def listar_livro_biblioteca():
    if not bibliotecas:
        print("Ainda não há bibliotecas cadastradas.")
        return

    lista_bibliotecas = exibir_lista_nomeada(bibliotecas)

    if not lista_bibliotecas:
        return

    escolha_biblioteca = input(
        "Digite o número da biblioteca ou 0 para cancelar: "
    )

    if escolha_biblioteca == "0":
        print("Ação cancelada.")
        return

    if escolha_biblioteca.isdigit():
        index = int(escolha_biblioteca)

        if index in lista_bibliotecas:
            nome_selecionado = lista_bibliotecas[index]
            instancia_biblioteca = bibliotecas[nome_selecionado]

            instancia_biblioteca.listar_livros()
        else:
            print("Número inválido.")
    else:
        print("Entrada inválida. Digite um número válido.")

def status_livro_biblioteca():
    lista_bibliotecas = exibir_lista_nomeada(bibliotecas)

    if not lista_bibliotecas:
        print("Ainda não há bibliotecas cadastradas.")
        return

    escolha_biblioteca = input(
        "Digite o número da biblioteca ou 0 para continuar: "
    )

    if escolha_biblioteca == "0":
        print("Ação cancelada.")
        return

    if escolha_biblioteca.isdigit():
        index = int(escolha_biblioteca)

        if index in lista_bibliotecas:
            nome_selecionado = lista_bibliotecas[index]
            instancia_biblioteca = bibliotecas[nome_selecionado]

            instancia_biblioteca.alterar_status()
        else:
            print("Número inválido.")
    else:
        print("Entrada inválida. Digite um número válido.")
