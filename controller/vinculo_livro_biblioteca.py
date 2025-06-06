from util import exibir_lista_bibliotecas, exibir_lista_nomeada
from data_store import bibliotecas, livros


def adicionar_livro_biblioteca():
    if not bibliotecas:
        return "Ainda não há bibliotecas cadastradas."

    lista_bibliotecas = exibir_lista_nomeada(bibliotecas)
    if not lista_bibliotecas:
        return

    escolha_biblioteca = input("Digite o número da biblioteca ou 0 para cancelar: ")
    if escolha_biblioteca == "0":
        return "Ação cancelada."

    if escolha_biblioteca.isdigit():
        index = int(escolha_biblioteca)
        if index in lista_bibliotecas:
            nome_biblioteca = lista_bibliotecas[index]
            instancia_biblioteca = bibliotecas[nome_biblioteca]

            if not livros:
                return "Ainda não há livros cadastrados."

            lista_livros = exibir_lista_nomeada(livros)
            if not lista_livros:
                return

            escolha_livro = input("Digite o número do livro: ")
            if escolha_livro.isdigit():
                index = int(escolha_livro)
                if index in lista_livros:
                    nome_livro = lista_livros[index]
                    instancia_livro = livros[nome_livro]

                    instancia_biblioteca.cadastrar_livro(instancia_livro)

                    return (
                        f"Livro '{nome_livro}' adicionado "
                        f"com sucesso na biblioteca '{nome_biblioteca}'."
                    )
                else:
                    return "Número inválido."
            else:
                return "Número inválido."
        else:
            return "Número inválido."
    else:
        return "Entrada inválida. Digite um número válido."

def remover_livro_biblioteca():
    lista_bibliotecas = exibir_lista_bibliotecas(bibliotecas)
    if not lista_bibliotecas:
        return "Ainda não há bibliotecas cadastradas."

    escolha_biblioteca = input(
        "Digite o número da biblioteca ou 0 para cancelar: "
    )

    if escolha_biblioteca == "0":
        return "Ação cancelada."

    if not escolha_biblioteca.isdigit():
        return "Entrada inválida."

    index = int(escolha_biblioteca)
    if index not in lista_bibliotecas:
        return "Número inválido."

    nome_biblioteca = lista_bibliotecas[index]
    biblioteca = bibliotecas[nome_biblioteca]

    if not biblioteca.livros:
        return f"A biblioteca '{nome_biblioteca}' não possui livros cadastrados."

    mensagem_livros = f"\nLivros da biblioteca '{nome_biblioteca}':\n"
    for i, registro in enumerate(biblioteca.livros, start=1):
        mensagem_livros += f"{i} - {registro['livro'].titulo}\n"
    print(mensagem_livros.strip())

    escolha_livro = input("Digite o número do livro que deseja remover: ")
    if not escolha_livro.isdigit():
        return "Entrada inválida."

    index_livro = int(escolha_livro)
    if index_livro < 1 or index_livro > len(biblioteca.livros):
        return "Número inválido."

    livro_remover = biblioteca.livros[index_livro - 1]["livro"]

    confirmacao = input(
        f"Tem certeza que deseja remover '{livro_remover.titulo}' "
        f"da biblioteca '{nome_biblioteca}'? (s/n): "
    ).strip().lower()

    if confirmacao == "s":
        return biblioteca.remover_livro(livro_remover)
    else:
        return "Remoção cancelada."

def listar_livro_biblioteca():
    if not bibliotecas:
        return "Ainda não há bibliotecas cadastradas."

    lista_bibliotecas = exibir_lista_nomeada(bibliotecas)

    if not lista_bibliotecas:
        return

    escolha_biblioteca = input(
        "Digite o número da biblioteca ou 0 para cancelar: "
    )

    if escolha_biblioteca == "0":
        return "Ação cancelada."

    if escolha_biblioteca.isdigit():
        index = int(escolha_biblioteca)

        if index in lista_bibliotecas:
            nome_selecionado = lista_bibliotecas[index]
            instancia_biblioteca = bibliotecas[nome_selecionado]

            mensagem = instancia_biblioteca.listar_livros()
            return mensagem
        else:
            return "Número inválido."
    else:
        return "Entrada inválida. Digite um número válido."


def status_livro_biblioteca():
    lista_bibliotecas = exibir_lista_nomeada(bibliotecas)

    if not lista_bibliotecas:
        return "Ainda não há bibliotecas cadastradas."

    escolha_biblioteca = input("Digite o número da biblioteca ou 0 para cancelar: ")

    if escolha_biblioteca == "0":
        return "Ação cancelada."

    if not escolha_biblioteca.isdigit():
        return "Entrada inválida. Digite um número válido."

    index = int(escolha_biblioteca)

    if index not in lista_bibliotecas:
        return "Número inválido."

    nome_selecionado = lista_bibliotecas[index]
    instancia_biblioteca = bibliotecas[nome_selecionado]

    mensagem = instancia_biblioteca.alterar_status()
    return mensagem

