from model.biblioteca import Biblioteca
from model.livro import Livro

from view.menu_biblioteca import menu_biblioteca
import util

livros = []
bibliotecas = []

if __name__ == "__main__":
    while True:
        menu_biblioteca()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome_biblioteca = input("Digite o nome da biblioteca: ")
            biblioteca = Biblioteca(nome_biblioteca)
            bibliotecas.append(biblioteca)
        elif opcao == "2":
            nome_livro = input("Nome do livro: ")
            autor_livro = input("Autor do livro: ")
            genero_livro = input("Gênero do livro: ")
            edicao_livro = input("Edição do livro: ")
            serie_livro = input("Série do livro: ")
            paginas_livro = input("Páginas do livro: ")
            formato_livro = input("Formato do livro: ")
            livro = Livro(nome_livro, autor_livro, genero_livro, edicao_livro, serie_livro, paginas_livro, formato_livro)
            livros.append(livro)
        elif opcao == "4":
            print("Saindo...  Até a próxima!")
            break
        else:
            print("Opção inválida. Tente novamente.")
