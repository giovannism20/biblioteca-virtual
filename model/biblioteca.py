from uuid import uuid4
from enum import Enum

class EstadosLivro(Enum):
    DISPONIVEL = 1
    NAO_DISPONIVEL = 2

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.uuid = uuid4()
        self.livros = []

    def cadastrar_livro(self, livro):
        self.livros.append({"livro": livro, "status": EstadosLivro.DISPONIVEL})

    def listar_livros(self):
        if not self.livros:
            print(f"Nenhum livro cadastrado na biblioteca '{self.nome}'.")
            return

        print(f"\nLivros na biblioteca '{self.nome}':")
        for registro in self.livros:
            livro = registro["livro"]
            status = registro["status"]
            print(f"- {livro.titulo} [{status.name}]")

    def alterar_status(self):
        pass

    def buscar_livros(self):
        pass

    def exportar_lista(self):
        with open("biblioteca.txt", "w", encoding="utf-8") as f:
            for livro in self.livros:
                f.write(
                    f"{livro['titulo']} - {livro['autor']} "
                    f"[{livro['genero']}] - Status: {livro['status']}\n"
                )
        print("Lista exportada para 'biblioteca.txt'.")
