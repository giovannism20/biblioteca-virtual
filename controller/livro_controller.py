from model.livro import Livro

from util import exibir_lista_livros, buscar_livros, exibir_lista_nomeada
from view.menu_busca_livro import menu_busca_livro
from view.menu_altera_dados_livro import menu_altera_dados_livro
from data_store import bibliotecas, livros

def cadastrar_livro():
    titulo = input("Nome do livro: ")
    autor = input("Autor do livro: ")
    genero = input("Gênero do livro: ")
    edicao = input("Edição do livro: ")
    serie = input("Série do livro: ")
    paginas = input("Páginas do livro: ")
    formato = input("Formato do livro: ")

    dados_livro = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "edicao": edicao,
        "serie": serie,
        "paginas": paginas,
        "formato": formato,
    }

    instancia_livro = Livro(**dados_livro)

    livros[dados_livro["titulo"]] = instancia_livro
    return f"O livro '{titulo}' foi cadastrado com sucesso!"

def alterar_livro():
    lista_livros = exibir_lista_livros(livros)
    if not lista_livros:
        return "Ainda não há livros cadastrados."

    escolha = input("Digite o número do livro ou 0 para cancelar: ")

    if escolha == "0":
        return "Ação cancelada."

    if escolha.isdigit():
        index = int(escolha)
        if index in lista_livros:
            nome_livro = lista_livros[index]
            livro = livros[nome_livro]

            menu_altera_dados_livro(livro)

            campo = input("Escolha a opção: ")
            campos_disponiveis = {
                "1": ("titulo", livro.altera_titulo),
                "2": ("autor", livro.altera_autor),
                "3": ("genero", livro.altera_genero),
                "4": ("edicao", livro.altera_edicao),
                "5": ("serie", livro.altera_serie),
                "6": ("paginas", livro.altera_paginas),
                "7": ("formato", livro.altera_formato),
            }

            if campo == "0":
                return "Alteração cancelada."
            elif campo in campos_disponiveis:
                campo_nome, metodo = campos_disponiveis[campo]
                novo_valor = (
                    input(f"Digite o novo valor para '{campo_nome}': ")
                    .strip()
                )

                if campo_nome == "paginas" and not novo_valor.isdigit():
                    return "Número de páginas deve ser um número."
                else:
                    metodo(novo_valor)

                    if campo_nome == "titulo":
                        livros[novo_valor] = livros.pop(nome_livro)

                    return f" {campo_nome.capitalize()} atualizado com sucesso."
            else:
                return " Opção inválida."
        else:
            return "Número inválido."
    else:
        return "Entrada inválida. Digite um número válido."

def excluir_livro():
    lista_livros = exibir_lista_livros(livros)
    if not lista_livros:
        return "Ainda não há livros cadastrados."

    escolha = input(
        "Digite o número do livro que deseja "
        "excluir ou 0 para cancelar: ")

    if escolha == "0":
        return "Ação cancelada."

    if escolha.isdigit():
        index = int(escolha)
        if index in lista_livros:
            nome_livro = lista_livros[index]
            livro = livros [nome_livro]

            confirmacao = (
                input(
                    f"Tem certeza que deseja excluir o livro '{nome_livro}'? (s/n): "
                    ).strip().lower()
            )
            if confirmacao == "s":
                for biblioteca in bibliotecas.values():
                    biblioteca.remover_livro(livro)

                del livros[nome_livro]
                return f" Livro '{nome_livro}' excluído com sucesso."
            else:
                return " Exclusão cancelada."
        else:
            return "Número inválido."
    else:
        return "Entrada inválida. Digite um número válido."

def listar_livros_cadastrados():
    if not livros:
        return "Ainda não há livros cadastrados."

    exibir_lista_nomeada(livros)

def pesquisar_livro():
    menu_busca_livro()

    opcao_busca = input(
        "Digite o número da opção desejada "
        "ou 0 para cancelar: "
    )

    if opcao_busca == "0":
        return "Ação cancelada."

    opcoes = {"1": "titulo", "2": "autor", "3": "serie"}
    campo_busca = opcoes.get(opcao_busca)

    if not campo_busca:
        return "Opção inválida."

    termo = input(f"Digite o {campo_busca} do livro: ")
    mensagem = buscar_livros(campo_busca, termo, livros, bibliotecas)
    return mensagem
