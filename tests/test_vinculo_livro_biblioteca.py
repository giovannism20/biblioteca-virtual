from pytest import MonkeyPatch
from controller.vinculo_livro_biblioteca import (
    adicionar_livro_biblioteca,
    listar_livro_biblioteca,
    remover_livro_biblioteca,
    status_livro_biblioteca,
)
from data_store import livros, bibliotecas
from model.livro import Livro
from model.biblioteca import Biblioteca


def test_adicionar_livro_biblioteca(monkeypatch: MonkeyPatch):
    livros.clear()
    bibliotecas.clear()

    livro = Livro(
        titulo="Clean Code",
        autor="Robert",
        genero="Tech",
        edicao="1",
        serie="SW",
        paginas="450",
        formato="Físico",
    )
    biblioteca = Biblioteca("Central")

    livros["Clean Code"] = livro
    bibliotecas["Central"] = biblioteca

    monkeypatch.setattr(
        "controller.vinculo_livro_biblioteca.exibir_lista_nomeada",
        lambda d: {1: list(d.keys())[0]},
    )
    inputs = iter(["1", "1"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    resultado = adicionar_livro_biblioteca()

    assert (
        resultado
        == "Livro 'Clean Code' adicionado com sucesso na biblioteca 'Central'."
    )
    assert biblioteca.livros[0]["livro"] == livro


def test_remover_livro_biblioteca(monkeypatch: MonkeyPatch):
    livros.clear()
    bibliotecas.clear()

    livro = Livro(
        titulo="Clean Code",
        autor="Robert",
        genero="Tech",
        edicao="1",
        serie="SW",
        paginas="450",
        formato="Físico",
    )
    biblioteca = Biblioteca("Central")
    biblioteca.cadastrar_livro(livro)

    livros[livro.titulo] = livro
    bibliotecas[biblioteca.nome] = biblioteca

    monkeypatch.setattr(
        "controller.vinculo_livro_biblioteca.exibir_lista_bibliotecas",
        lambda d: {1: list(d.keys())[0]},
    )
    inputs = iter(["1", "1", "s"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    resultado = remover_livro_biblioteca()

    assert (
        resultado
        == f" Livro '{livro.titulo}' removido da biblioteca '{biblioteca.nome}'."
    )
    assert not biblioteca.livros


def test_listar_livro_biblioteca(monkeypatch: MonkeyPatch):
    livros.clear()
    bibliotecas.clear()

    livro = Livro(
        titulo="Clean Code",
        autor="Robert",
        genero="Tech",
        edicao="1",
        serie="SW",
        paginas="450",
        formato="Físico",
    )
    biblioteca = Biblioteca("Central")
    biblioteca.cadastrar_livro(livro)

    livros[livro.titulo] = livro
    bibliotecas[biblioteca.nome] = biblioteca

    monkeypatch.setattr(
        "controller.vinculo_livro_biblioteca.exibir_lista_nomeada",
        lambda d: {1: list(d.keys())[0]},
    )
    monkeypatch.setattr("builtins.input", lambda _: "1")

    resultado = listar_livro_biblioteca()

    assert livro.titulo in resultado


def test_status_livro_biblioteca(monkeypatch):
    livros.clear()
    bibliotecas.clear()

    livro = Livro(
        titulo="Clean Code",
        autor="Robert",
        genero="Tech",
        edicao="1",
        serie="SW",
        paginas="450",
        formato="Físico",
    )
    biblioteca = Biblioteca("Central")
    biblioteca.cadastrar_livro(livro)

    livros[livro.titulo] = livro
    bibliotecas[biblioteca.nome] = biblioteca

    monkeypatch.setattr(
        "controller.vinculo_livro_biblioteca.exibir_lista_nomeada",
        lambda d: {1: list(d.keys())[0]},
    )
    monkeypatch.setattr("builtins.input", lambda _: "1")
    monkeypatch.setattr(
        biblioteca, "alterar_status", lambda: "Status atualizado com sucesso."
    )

    resultado = status_livro_biblioteca()

    assert resultado == "Status atualizado com sucesso."
