import os

livros = []

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print("\n GERENCIADOR DE BIBLIOTECA ")
    print("1. Cadastrar livro")
    print("2. Listar livros")
    print("3. Alterar status do livro")
    print("4. Buscar livros")
    print("5. Exportar para arquivo")
    print("6. Sair")

def cadastrar_livro():
    titulo = input("Título do livro: ")
    autor = input("Autor: ")
    genero = input("Gênero: ")
    status = input("Status (lido, lendo, a ler): ").lower()
    livro = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "status": status
    }
    livros.append(livro)
    print(" Livro cadastrado com sucesso!")

def listar_livros():
    if not livros:
        print("Nenhum livro cadastrado.")
        return
    print("\n Lista de livros:")
    for i, livro in enumerate(livros, 1):
        print(f"{i}. {livro['titulo']} - {livro['autor']} [{livro['genero']}] - Status: {livro['status']}")

def alterar_status():
    listar_livros()
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

def buscar_livros():
    campo = input("Buscar por (autor/genero/status): ").lower()
    valor = input(f"Digite o valor para buscar em {campo}: ").lower()
    encontrados = [livro for livro in livros if livro.get(campo, '').lower() == valor]

    if encontrados:
        print(f"\n Livros encontrados ({len(encontrados)}):")
        for livro in encontrados:
            print(f"{livro['titulo']} - {livro['autor']} [{livro['genero']}] - Status: {livro['status']}")
    else:
        print("Nenhum livro encontrado com esse critério.")

def exportar_lista():
    with open("biblioteca.txt", "w", encoding="utf-8") as f:
        for livro in livros:
            f.write(f"{livro['titulo']} - {livro['autor']} [{livro['genero']}] - Status: {livro['status']}\n")
    print(" Lista exportada para 'biblioteca.txt'.")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        limpar_tela()

        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            alterar_status()
        elif opcao == "4":
            buscar_livros()
        elif opcao == "5":
            exportar_lista()
        elif opcao == "6":
            print("Saindo...  Até a próxima!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
