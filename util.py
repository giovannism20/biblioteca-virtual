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

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
