import os

def exibir_lista_bibliotecas(bibliotecas: dict) -> list:
    if not bibliotecas:
        print("Ainda não possuímos bibliotecas cadastradas no sistema.")
        return []

    print("Selecione a biblioteca pelo número:")
    lista = list(bibliotecas.keys())
    for i, nome in enumerate(lista, start=1):
        print(f"{i} - {nome}")
    return lista

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
