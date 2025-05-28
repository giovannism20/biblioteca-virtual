from uuid import uuid4
from enum import enum

class EstadosLivro(Enum):
    DISPONIVEL = 1
    NAO_DISPONIVEL = 2

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.uuid = uuid4()
        self.livros = []

    def cadastrar_livro(self, livro):
        self.livros.append({livro, status: EstadosLivro.DISPONIVEL})

    def listar_livros(self):
        return self.livros

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
