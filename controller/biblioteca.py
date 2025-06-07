from model.biblioteca import Biblioteca

from util import exibir_lista_bibliotecas, exibir_lista_nomeada
from data_store import bibliotecas

def cadastrar_biblioteca():
    nome_biblioteca = input("Digite o nome da biblioteca: ")
    instancia_biblioteca = Biblioteca(nome_biblioteca)
    bibliotecas[nome_biblioteca] = instancia_biblioteca
    return f"A biblioteca '{nome_biblioteca}' foi cadastrada com sucesso!"

def alterar_nome_biblioteca():
    lista_bibliotecas = exibir_lista_bibliotecas(bibliotecas)

    if not lista_bibliotecas:
        return "Ainda não há bibliotecas cadastradas."

    escolha = input("Digite o número da biblioteca ou 0 para cancelar: ")

    if escolha == "0":
        return "Ação cancelada."

    if escolha.isdigit():
        index = int(escolha)

        if index in lista_bibliotecas:
            nome_antigo = lista_bibliotecas[index]
            instancia_biblioteca = bibliotecas[nome_antigo]

            novo_nome = input("Digite o novo nome da biblioteca: ").strip()

            if novo_nome:
                instancia_biblioteca.alterar_nome(novo_nome)
                bibliotecas[novo_nome] = instancia_biblioteca
                del bibliotecas[nome_antigo]
                return f"Nome da biblioteca alterado para '{novo_nome}' com sucesso!"
            else:
                return "Nome inválido."
        else:
            return "Número inválido."
    else:
        return "Entrada inválida. Digite um número válido."

def excluir_biblioteca():
    lista_bibliotecas = exibir_lista_bibliotecas(bibliotecas)
    if not lista_bibliotecas:
        return "Ainda não há bibliotecas cadastradas."

    escolha = (
        input(
            "Digite o número da biblioteca que deseja "
            "excluir ou 0 para cancelar: ")
    )
    if escolha == "0":
        return "Ação cancelada."

    if escolha.isdigit():
        index = int(escolha)
        if index in lista_bibliotecas:
            nome_excluir = lista_bibliotecas[index]
            confirmacao = (
                input(f"Tem certeza que deseja excluir '{nome_excluir}'?(s/n): ")
                .strip()
                .lower()
            )
            if confirmacao == "s":
                del bibliotecas[nome_excluir]
                return f"Biblioteca '{nome_excluir}' removida com sucesso."
            else:
                return "Ação cancelada."
        else:
            return "Número inválido."
    else:
        return "Entrada inválida. Digite um número válido."

def listar_bibliotecas_cadastradas():
    if not bibliotecas:
        return "Ainda não há bibliotecas cadastradas."

    return exibir_lista_nomeada(bibliotecas)
