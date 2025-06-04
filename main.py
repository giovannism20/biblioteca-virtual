from model.biblioteca import Biblioteca
from model.livro import Livro

from util import exibir_lista_bibliotecas, exibir_lista_livros, buscar_livros, exibir_lista_nomeada
from view.menu_biblioteca import menu_biblioteca
from view.menu_busca_livro import menu_busca_livro
from view.menu_altera_dados_livro import menu_altera_dados_livro

livros = {}
bibliotecas = {}

if __name__ == "__main__":
    while True:
        menu_biblioteca()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome_biblioteca = input("Digite o nome da biblioteca: ")
            instancia_biblioteca = Biblioteca(nome_biblioteca)
            bibliotecas[nome_biblioteca] = instancia_biblioteca
        elif opcao == "2":
            lista_bibliotecas = exibir_lista_bibliotecas(bibliotecas)
            if not lista_bibliotecas:
                continue

            escolha = input("Digite o número da biblioteca ou 0 para cancelar: ")

            if escolha == "0":
                print("Ação cancelada.")
                continue
            if escolha.isdigit():
                index = int(escolha) - 1
                if 0 <= index < len(lista_bibliotecas):
                    nome_antigo = lista_bibliotecas[index]
                    instancia_biblioteca = bibliotecas[nome_antigo]

                    novo_nome = input("Digite o novo nome da biblioteca: ").strip()

                    if novo_nome:
                        instancia_biblioteca.alterar_nome(novo_nome)
                        bibliotecas[novo_nome] = instancia_biblioteca
                        del bibliotecas[nome_antigo]
                    else:
                        print("Nome inválido.")
                else:
                    print("Número inválido.")
            else:
                print("Entrada inválida. Digite um número válido.")
        elif opcao == "3":
            lista_bibliotecas = exibir_lista_bibliotecas(bibliotecas)
            if not lista_bibliotecas:
                continue

            escolha = (
                input(
                    f"Digite o número da biblioteca que deseja "
                    f"excluir ou 0 para cancelar: ")
            )
            if escolha == "0":
                print("Ação cancelada.")
                continue
            if escolha.isdigit():
                index = int(escolha) - 1
                if 0 <= index < len(lista_bibliotecas):
                    nome_excluir = lista_bibliotecas[index]
                    confirmacao = (
                        input(f"Tem certeza que deseja excluir '{nome_excluir}'?(s/n): ")
                        .strip()
                        .lower()
                    )
                    if confirmacao == "s":
                        del bibliotecas[nome_excluir]
                        print(f"Biblioteca '{nome_excluir}' removida com sucesso.")
                    else:
                        print("Ação cancelada.")
                else:
                    print("Número inválido.")
            else:
                print("Entrada inválida. Digite um número válido.")
        elif opcao == "4":
            if not bibliotecas:
                continue

            exibir_lista_nomeada(bibliotecas)
        elif opcao == "5":
            titulo = input("Nome do livro: ")
            autor = input("Autor do livro: ")
            genero = input("Gênero do livro: ")
            edicao = input("Edição do livro: ")
            serie = input("Série do livro: ")
            paginas = input("Páginas do livro: ")
            formato = input("Formato do livro: ")

            dados_livro = {
                "titulo": titulo,
                "autor": autor,
                "genero": genero,
                "edicao": edicao,
                "serie": serie,
                "paginas": paginas,
                "formato": formato,
            }

            instancia_livro = Livro(**dados_livro)

            livros[dados_livro["titulo"]] = instancia_livro
        elif opcao == "6":
            lista_livros = exibir_lista_livros(livros)
            if not lista_livros:
                continue

            escolha = input("Digite o número do livro ou 0 para cancelar: ")

            if escolha == "0":
                print("Ação cancelada.")
                continue

            if escolha.isdigit():
                index = int(escolha) - 1
                if 0 <= index < len(lista_livros):
                    nome_livro = lista_livros[index]
                    livro = livros[nome_livro]

                    menu_altera_dados_livro(livro)

                    campo = input("Escolha a opção: ")
                    campos_disponiveis = {
                        "1": ("titulo", livro.altera_titulo),
                        "2": ("autor", livro.altera_autor),
                        "3": ("genero", livro.altera_genero),
                        "4": ("edicao", livro.altera_edicao),
                        "5": ("serie", livro.altera_serie),
                        "6": ("paginas", livro.altera_paginas),
                        "7": ("formato", livro.altera_formato),
                    }

                    if campo == "0":
                        print("Alteração cancelada.")
                    elif campo in campos_disponiveis:
                        campo_nome, metodo = campos_disponiveis[campo]
                        novo_valor = (
                            input(f"Digite o novo valor para '{campo_nome}': ")
                            .strip()
                        )

                        if campo_nome == "paginas" and not novo_valor.isdigit():
                            print("Número de páginas deve ser um número.")
                        else:
                            metodo(novo_valor)

                            if campo_nome == "titulo":
                                livros[novo_valor] = livros.pop(nome_livro)

                            print(f" {campo_nome.capitalize()} atualizado com sucesso.")
                    else:
                        print(" Opção inválida.")
                else:
                    print("Número inválido.")
            else:
                print("Entrada inválida. Digite um número válido.")
        elif opcao == "7":
            lista_livros = exibir_lista_livros(livros)
            if not lista_livros:
                continue

            escolha = input(
                f"Digite o número do livro que deseja "
                f"excluir ou 0 para cancelar: ")

            if escolha == "0":
                print("Ação cancelada.")
                continue

            if escolha.isdigit():
                index = int(escolha) - 1
                if 0 <= index < len(lista_livros):
                    nome_livro = lista_livros[index]
                    livro = livros [nome_livro]

                    confirmacao = (
                        input(
                            f"Tem certeza que deseja excluir o livro '{nome_livro}'? (s/n): "
                            ).strip().lower()
                    )
                    if confirmacao == "s":
                        for biblioteca in bibliotecas.values():
                            biblioteca.remover_livro(livro)

                        del livros[nome_livro]
                        print(f" Livro '{nome_livro}' excluído com sucesso.")
                    else:
                        print(" Exclusão cancelada.")
                else:
                    print("Número inválido.")
            else:
                print("Entrada inválida. Digite um número válido.")
        elif opcao == "8":
            if not livros:
                print("Ainda não há livros cadastrados.")
                continue

            exibir_lista_nomeada(livros)
        elif opcao == "9":
            if not bibliotecas:
                print("Ainda não há bibliotecas cadastradas.")
                continue

            lista_bibliotecas = exibir_lista_nomeada(bibliotecas)

            if not lista_bibliotecas:
                continue

            escolha_biblioteca = input(
                "Digite o número da biblioteca ou 0 para cancelar: "
            )

            if escolha_biblioteca == "0":
                print("Ação cancelada.")
                continue

            if escolha_biblioteca.isdigit():
                index = int(escolha_biblioteca) - 1

                if 0 <= index < len(lista_bibliotecas):
                    nome_selecionado = lista_bibliotecas[index]
                    instancia_biblioteca = bibliotecas[nome_selecionado]

                    if not livros:
                        print("Ainda não há livros cadastrados.")
                        continue

                    lista_livros = exibir_lista_nomeada(livros)

                    if not lista_livros:
                        continue

                    escolha_livro = input("Digite o número do livro: ")

                    if escolha_livro.isdigit():
                        index = int(escolha_livro) - 1

                        if 0 <= index < len(lista_livros):
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
        elif opcao == "10":
            lista_bibliotecas = exibir_lista_bibliotecas(bibliotecas)
            if not lista_bibliotecas:
                continue

            escolha_biblioteca = input(
                f"Digite o número da biblioteca"
                f"ou 0 para cancelar: ")

            if escolha_biblioteca == "0":
                print("Ação cancelada.")
                continue

            if not escolha_biblioteca.isdigit():
                print("Entrada inválida.")
                continue

            index = int(escolha_biblioteca) - 1
            if not 0 <= index < len(lista_bibliotecas):
                print("Número inválido.")
                continue

            nome_biblioteca = lista_bibliotecas[index]
            biblioteca = bibliotecas[nome_biblioteca]

            if not biblioteca.livros:
                print(f"A biblioteca '{nome_biblioteca}' não possui livros cadastrados.")
                continue

            print(f"\nLivros da biblioteca '{nome_biblioteca}':")
            for i, registro in enumerate(biblioteca.livros, start=1):
                print(f"{i} - {registro['livro'].titulo}")

            escolha_livro = input("Digite o número do livro que deseja remover: ")
            if not escolha_livro.isdigit():
                print("Entrada inválida.")
                continue

            index_livro = int(escolha_livro) - 1
            if not 0 <= index_livro < len(biblioteca.livros):
                print("Número inválido.")
                continue

            livro_remover = biblioteca.livros[index_livro]["livro"]

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
        elif opcao == "11":
            if not bibliotecas:
                print("Ainda não há bibliotecas cadastradas.")
                continue

            lista_bibliotecas = exibir_lista_nomeada(bibliotecas)

            if not lista_bibliotecas:
                continue

            escolha_biblioteca = input(
                "Digite o número da biblioteca ou 0 para cancelar: "
            )

            if escolha_biblioteca == "0":
                print("Ação cancelada.")
                continue

            if escolha_biblioteca.isdigit():
                index = int(escolha_biblioteca) - 1

                if 0 <= index < len(lista_bibliotecas):
                    nome_selecionado = lista_bibliotecas[index]
                    instancia_biblioteca = bibliotecas[nome_selecionado]

                    instancia_biblioteca.listar_livros()
                else:
                    print("Número inválido.")
            else:
                print("Entrada inválida. Digite um número válido.")
        elif opcao == "12":
            if not lista_bibliotecas:
                continue

            lista_bibliotecas = exibir_lista_nomeada(bibliotecas)

            escolha_biblioteca = input(
                "Digite o número da biblioteca ou 0 para continuar: "
            )

            if escolha_biblioteca == "0":
                print("Ação cancelada.")
                continue

            if escolha_biblioteca.isdigit():
                index = int(escolha_biblioteca) - 1

                if 0 <= index < len(lista_bibliotecas):
                    nome_selecionado = lista_bibliotecas[index]
                    instancia_biblioteca = bibliotecas[nome_selecionado]

                    instancia_biblioteca.alterar_status()
                else:
                    print("Número inválido.")
            else:
                print("Entrada inválida. Digite um número válido.")
        elif opcao == "13":
            menu_busca_livro()

            opcao_busca = input(
                f"Digite o número da opção desejada "
                f"ou 0 para cancelar: ")

            if opcao_busca == "0":
                print("Ação cancelada.")
                continue

            opcoes = {"1": "titulo", "2": "autor", "3": "serie"}
            campo_busca = opcoes.get(opcao_busca)

            if not campo_busca:
                print("Opção inválida.")
                continue

            termo = input(f"Digite o {campo_busca} do livro: ")
            buscar_livros(campo_busca, termo, livros, bibliotecas)
        elif opcao == "14":
            print("Saindo...  Até a próxima!")
            break
        else:
            print("Opção inválida. Tente novamente.")
