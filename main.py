from model.biblioteca import Biblioteca
from model.livro import Livro

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
        elif opcao == "3":
            for i, nome_biblioteca in enumerate(bibliotecas.keys(), start=1):
                print(f"{i} - {nome_biblioteca}")
        elif opcao == "4":
            for i, nome_livro in enumerate(livros.keys(), start=1):
                print(f"{i} - {nome_livro}")
        elif opcao == "5":
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
        elif opcao == "6":
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
        elif opcao == "7":
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
        elif opcao == "8":
            print("\nComo deseja buscar o livro?")
            print("1 - Por Título")
            print("2 - Por Autor")
            print("3 - Por Série")

            opcao_busca = input("Digite o número da opção desejada: ")

            if opcao_busca == "1":
                campo_busca = "titulo"
            elif opcao_busca == "2":
                campo_busca = "autor"
            elif opcao_busca == "3":
                campo_busca = "serie"
            else:
                print("Opção inválida.")
                continue

            termo = input(f"Digite o {campo_busca} do livro: ")

            Livro.buscar_livros(
                campo_busca,
                termo,
                livros,
                bibliotecas
            )
        elif opcao == "9":
            print("Saindo...  Até a próxima!")
            break
        else:
            print("Opção inválida. Tente novamente.")
