from uuid import uuid4

class Biblioteca:
    def __init__(self, nome):
        self.uuid = uuid4()
        self.nome = nome
        self.livros = []

    def cadastrar_livro(self, livro):
        livros.append(livro)

    def listar_livros(self):
        if not livros:
            print("Nenhum livro cadastrado.")
            return
        print("\n Lista de livros:")
        for i, livro in enumerate(livros, 1):
            print(f"{i}. {livro['titulo']} - {livro['autor']} [{livro['genero']}] - Status: {livro['status']}")

    def alterar_status(self):
        self.listar_livros()
        if not livros:
            return
        try:
            i = int(input("Digite o número do livro para alterar o status: ")) - 1
            if 0 <= i < len(livros):
                novo_status = input("Novo status (lido, lendo, a ler): ").lower()
                livros[i]['status'] = novo_status
                print(" Status atualizado.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida.")

    def buscar_livros(self):
        campo = input("Buscar por (autor/genero/status): ").lower()
        valor = input(f"Digite o valor para buscar em {campo}: ").lower()
        encontrados = [livro for livro in livros if livro.get(campo, '').lower() == valor]

        if encontrados:
            print(f"\n Livros encontrados ({len(encontrados)}):")
            for livro in encontrados:
                print(f"{livro['titulo']} - {livro['autor']} [{livro['genero']}] - Status: {livro['status']}")
        else:
            print("Nenhum livro encontrado com esse critério.")

    def exportar_lista(self):
        with open("biblioteca.txt", "w", encoding="utf-8") as f:
            for livro in livros:
                f.write(f"{livro['titulo']} - {livro['autor']} [{livro['genero']}] - Status: {livro['status']}\n")
        print(" Lista exportada para 'biblioteca.txt'.")

