from model.biblioteca import Biblioteca
from model.livro import Livro

from util import exibir_lista_bibliotecas
from view.menu_biblioteca import menu_biblioteca

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

            escolha = input("Digite o número da biblioteca: ")

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

            escolha = input("Digite o número da biblioteca que deseja excluir: ")

            if escolha.isdigit():
                index = int(escolha) - 1
                if 0 <= index < len(lista_bibliotecas):
                    nome_excluir = lista_bibliotecas[index]
                    confirmacao = input(f"Tem certeza que deseja excluir '{nome_excluir}'? (s/n): ").strip().lower()
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
            for i, nome_biblioteca in enumerate(bibliotecas.keys(), start=1):
                print(f"{i} - {nome_biblioteca}")
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
            pass
        elif opcao == "7":
            pass
        elif opcao == "8":
            for i, nome_livro in enumerate(livros.keys(), start=1):
                print(f"{i} - {nome_livro}")
        elif opcao == "9":
            if not bibliotecas or not livros:
                print("Ainda não possuímos bibliotecas cadastradas no sistema.")

            print("Selecione a biblioteca pelo número: ")
            lista_bibliotecas = list(bibliotecas.keys())

            for i, nome_biblioteca in enumerate(lista_bibliotecas, start=1):
                print(f"{i} - {nome_biblioteca}")

            escolha_biblioteca = input("Digite o número da biblioteca: ")

            if escolha_biblioteca.isdigit():
                index = int(escolha_biblioteca) - 1

                if 0 <= index < len(lista_bibliotecas):
                    nome_selecionado = lista_bibliotecas[index]
                    instancia_biblioteca = bibliotecas[nome_selecionado]

                    print("Selecione o livro pelo número: ")
                    lista_livros = list(livros.keys())

                    for i, nome_livro in enumerate(lista_livros, start=1):
                        print(f"{i} - {nome_livro}")

                    escolha_biblioteca = input("Digite o número do livro: ")

                    if escolha_biblioteca.isdigit():
                        index = int(escolha_biblioteca) - 1

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
            pass
        elif opcao == "11":
            if not bibliotecas:
                print("Ainda não possuímos bibliotecas cadastradas no sistema.")
            else:
                print("Selecione a biblioteca pelo número:")
                lista_bibliotecas = list(bibliotecas.keys())

                for i, nome_biblioteca in enumerate(lista_bibliotecas, start=1):
                    print(f"{i} - {nome_biblioteca}")

                escolha_biblioteca = input("Digite o número da biblioteca: ")

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
            if not bibliotecas:
                print("Ainda não possuímos bibliotecas cadastradas no sistema.")
            else:
                print("Selecione a biblioteca pelo número:")
                lista_bibliotecas = list(bibliotecas.keys())

                for i, nome_biblioteca in enumerate(lista_bibliotecas, start=1):
                    print(f"{i} - {nome_biblioteca}")

                escolha_biblioteca = input("Digite o número da biblioteca: ")

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
            print("\nComo deseja buscar o livro?")
            print("1 - Por Título")
            print("2 - Por Autor")
            print("3 - Por Série")

            opcao_busca = input("Digite o número da opção desejada: ")

            opcoes = {"1": "titulo", "2": "autor", "3": "serie"}
            campo_busca = opcoes.get(opcao_busca)

            if not campo_busca:
                print("Opção inválida.")
                continue

            termo = input(f"Digite o {campo_busca} do livro: ")
            Livro.buscar_livros(campo_busca, termo, livros, bibliotecas)
        elif opcao == "14":
            print("Saindo...  Até a próxima!")
            break
        else:
            print("Opção inválida. Tente novamente.")
