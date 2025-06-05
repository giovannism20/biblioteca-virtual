from model.biblioteca import Biblioteca

from util import exibir_lista_bibliotecas, exibir_lista_livros, buscar_livros, exibir_lista_nomeada
from view.menu_biblioteca import menu_biblioteca
from data_store import bibliotecas

def cadastrar_biblioteca():
    nome_biblioteca = input("Digite o nome da biblioteca: ")
    instancia_biblioteca = Biblioteca(nome_biblioteca)
    bibliotecas[nome_biblioteca] = instancia_biblioteca
    print(f"A biblioteca '{nome_biblioteca}' foi cadastrada com sucesso!")

def alterar_nome_biblioteca():
    lista_bibliotecas = exibir_lista_bibliotecas(bibliotecas)

    if not lista_bibliotecas:  
        print("Ainda não há bibliotecas cadastradas.")
        return    

    escolha = input("Digite o número da biblioteca ou 0 para cancelar: ")

    if escolha == "0":
        print("Ação cancelada.")
        return

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
            else:
                print("Nome inválido.")
        else:
            print("Número inválido.")
    else:
        print("Entrada inválida. Digite um número válido.")

def excluir_biblioteca():
    lista_bibliotecas = exibir_lista_bibliotecas(bibliotecas)
    if not lista_bibliotecas:
        print("Ainda não há bibliotecas cadastradas.")
        return

    escolha = (
        input(
            "Digite o número da biblioteca que deseja "
            "excluir ou 0 para cancelar: ")
    )
    if escolha == "0":
        print("Ação cancelada.")
        return
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
                print(f"Biblioteca '{nome_excluir}' removida com sucesso.")
            else:
                print("Ação cancelada.")
        else:
            print("Número inválido.")
    else:
        print("Entrada inválida. Digite um número válido.")

def listar_bibliotecas_cadastradas():
    if not bibliotecas:
        print("Ainda não há bibliotecas cadastradas.")
        return

    exibir_lista_nomeada(bibliotecas)
