import os

def exibir_lista_nomeada(entidades: dict, mensagem_vazia: str) -> list:
    if not entidades:
        print(mensagem_vazia)
        return []

    lista = list(entidades.keys())
    for i, nome in enumerate(lista, start=1):
        print(f"{i} - {nome}")
    return lista

def exibir_lista_livros(livros: dict) -> list:
    return exibir_lista_nomeada(
        livros,
        "Ainda não há livros cadastrados no sistema."
    )

def exibir_lista_bibliotecas(bibliotecas: dict) -> list:
    return exibir_lista_nomeada(
        bibliotecas,
        "Ainda não há bibliotecas cadastradas no sistema."
    )

def buscar_livros(campo, termo, livros, bibliotecas):
    resultados = []

    for titulo, livro in livros.items():
        if getattr(livro, campo).strip().lower() == termo.strip().lower():
            print(f"Livro encontrado: {titulo}")
            bibliotecas_encontradas = []

            for nome_biblioteca, biblioteca in bibliotecas.items():
                for registro in biblioteca.livros:
                    if registro["livro"] == livro:
                        bibliotecas_encontradas.append(

                            (
                                nome_biblioteca,
                                registro["status"].name
                            )
                        )
            resultados.append((livro, bibliotecas_encontradas))

    if resultados:
        print(f"\n Resultado da busca por {campo} '{termo}':\n")
        for livro, lista_bibliotecas in resultados:
            print(f"  Título: {livro.titulo}")
            print(f"  Autor: {livro.autor}")
            print(f"  Gênero: {livro.genero}")
            print(f"  Edição: {livro.edicao}")
            print(f"  Série: {livro.serie}")
            print(f"  Páginas: {livro.paginas}")
            print(f"  Formato: {livro.formato}")
            if lista_bibliotecas:
                print("  Bibliotecas onde está cadastrado:")
                for nome, status in lista_bibliotecas:
                    print(f"  s- {nome} [{status}]")
            else:
                print("  Sem vinculo a nenhuma biblioteca.\n")
    else:
        print(f"  Nenhum livro encontrado com {campo} '{termo}'.")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
