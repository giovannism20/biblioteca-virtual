from model.biblioteca import Biblioteca
from model.livro import Livro

from view.menu_biblioteca import menu_biblioteca
import util

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
            nome_livro = input("Nome do livro: ")
            autor_livro = input("Autor do livro: ")
            genero_livro = input("Gênero do livro: ")
            edicao_livro = input("Edição do livro: ")
            serie_livro = input("Série do livro: ")
            paginas_livro = input("Páginas do livro: ")
            formato_livro = input("Formato do livro: ")
            instancia_livro = Livro(
                nome_livro,
                autor_livro,
                genero_livro,
                edicao_livro,
                serie_livro,
                paginas_livro,
                formato_livro
            )

            livros[nome_livro] = instancia_livro
        elif opcao == "3":
            for i, nome_biblioteca in enumerate(bibliotecas.keys(), start=1):
                print(f"{i} - {nome_biblioteca}")
        elif opcao == "4":
            for i, nome_livro in enumerate(livros.keys(), start=1):
                print(f"{i} - {nome_livro}")
        elif opcao == "5":
            if not bibliotecas:
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
                            instancia_livro_test = livros[nome_selecionado]

                            instancia_biblioteca.cadastrar_livro(instancia_livro_test)
                            instancia_biblioteca.listar_livros
                    else:
                        print("Número inválido.")
                else:
                    print("Número inválido.")
            else:
                print("Entrada inválida. Digite um número válido.")
        elif opcao == "6":
            print("Saindo...  Até a próxima!")
            break
        else:
            print("Opção inválida. Tente novamente.")
