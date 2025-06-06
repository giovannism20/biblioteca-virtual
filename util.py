import os

def exibir_lista_nomeada(entidade: dict):
    entidade_enumerada = {}
    for index, nome in enumerate(entidade, start=1):
        entidade_enumerada[index] = nome
        print(f"{index} - {nome}")
    return entidade_enumerada

def exibir_lista_livros(livros: dict) -> list:
    return exibir_lista_nomeada(livros)

def exibir_lista_bibliotecas(bibliotecas: dict) -> list:
    return exibir_lista_nomeada(bibliotecas)

def buscar_livros(campo, termo, livros, bibliotecas):
    resultados = []

    for titulo, livro in livros.items():
        if getattr(livro, campo).strip().lower() == termo.strip().lower():
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
        mensagem = f"\nResultado da busca por {campo} '{termo}':\n\n"
        for livro, lista_bibliotecas in resultados:
            mensagem += f"  Título: {livro.titulo}\n"
            mensagem += f"  Autor: {livro.autor}\n"
            mensagem += f"  Gênero: {livro.genero}\n"
            mensagem += f"  Edição: {livro.edicao}\n"
            mensagem += f"  Série: {livro.serie}\n"
            mensagem += f"  Páginas: {livro.paginas}\n"
            mensagem += f"  Formato: {livro.formato}\n"
            if lista_bibliotecas:
                mensagem += "  Bibliotecas onde está cadastrado:\n"
                for nome, status in lista_bibliotecas:
                    mensagem += f"  s- {nome} [{status}]\n"
            else:
                mensagem += "  Sem vínculo a nenhuma biblioteca.\n"
            mensagem += "\n"  # Linha em branco para separar livros
        return mensagem
    else:
        return f"Nenhum livro encontrado com {campo} '{termo}'."


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
