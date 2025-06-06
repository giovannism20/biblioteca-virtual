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

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def cadastrar_livro(self, livro):
        self.livros.append({"livro": livro, "status": EstadosLivro.DISPONIVEL})

    def listar_livros(self):
        if not self.livros:
            return f"Nenhum livro cadastrado na biblioteca '{self.nome}'."

        mensagem = f"\nLivros na biblioteca '{self.nome}':\n"
        for registro in self.livros:
            livro = registro["livro"]
            status = registro["status"]
            mensagem += f"- {livro.titulo} [{status.name}]\n"
        return mensagem.strip()

    def alterar_status(self):
        if not self.livros:
            return f"Nenhum livro cadastrado na biblioteca '{self.nome}'."

        mensagem = f"\nSelecione o livro para alterar o status na biblioteca '{self.nome}':\n"
        for i, registro in enumerate(self.livros, start=1):
            livro = registro["livro"]
            status = registro["status"]
            mensagem += f"{i} - {livro.titulo} [{status.name}]\n"

        print(mensagem)

        escolha = input("Digite o número do livro: ")

        if not escolha.isdigit():
            return "Entrada inválida. Digite um número válido."

        index = int(escolha) - 1
        if not (0 <= index < len(self.livros)):
            return "Número inválido."

        registro = self.livros[index]
        status_atual = registro["status"]
        novo_status = (
            EstadosLivro.NAO_DISPONIVEL
            if status_atual == EstadosLivro.DISPONIVEL
            else EstadosLivro.DISPONIVEL
        )
        registro["status"] = novo_status

        return (
            f"Status do livro '{registro['livro'].titulo}' "
            f"alterado para [{novo_status.name}]."
        )

    def remover_livro(self, livro_para_remover) -> str:
        for registro in self.livros:
            if registro["livro"] == livro_para_remover:
                self.livros.remove(registro)
                return f" Livro '{livro_para_remover.titulo}' removido da biblioteca '{self.nome}'."

        return f" Livro '{livro_para_remover.titulo}' não encontrado na biblioteca '{self.nome}'."

    def exportar_lista(self):
        with open("biblioteca.txt", "w", encoding="utf-8") as f:
            for livro in self.livros:
                f.write(
                    f"{livro['titulo']} - {livro['autor']} "
                    f"[{livro['genero']}] - Status: {livro['status']}\n"
                )
        return "Lista exportada para 'biblioteca.txt'."
